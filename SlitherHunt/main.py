

import pygame
import random
from settings import *
from snake import Snake
from enemy import Enemy
from agent_brain import AgentBrain

def load_highscore():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0
    
def save_highscore(score):
    with open ("highscore.txt", "w") as f:
        f.write(str(score))


class Food:
    def __init__(self, snake_body, enemy_pos):
        self.respawn(snake_body,enemy_pos)
        

    def respawn(self, snake_body, enemy_pos):
        free_cells = []
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                pos = [x, y]
                if pos not in snake_body and pos != enemy_pos: ##############
                    free_cells.append(pos)
        
        if not free_cells:
            # win condition
            print("YOU WIN — NO SPACE LEFT")
            self.position = None
            return


        self.position = random.choice(free_cells)

        
        

    def draw(self, surface):
        if self.position is None:
            return
        
        pygame.draw.rect(
            surface,
            YELLOW,
            (self.position[0] * CELL_SIZE,
             self.position[1] * CELL_SIZE + SCORE_BAR_HEIGHT,
            CELL_SIZE, CELL_SIZE)
        )


def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Slither Hunt")

    clock = pygame.time.Clock()

    snake = Snake()
    enemy = Enemy()
    food = Food(snake.body, enemy.position)
    agent = AgentBrain()

    Enemy_Move_Delay = 100
    last_enemy_move = 0

    score = 0
    highscore = load_highscore()
    running = True


    font = pygame.font.SysFont("Arial", 24)

    while running:

        # Input

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN: ##################
                if event.key == pygame.K_w:
                    snake.change_direction("UP")
                if event.key == pygame.K_s:
                    snake.change_direction("DOWN")
                if event.key == pygame.K_a:
                    snake.change_direction("LEFT")
                if event.key == pygame.K_d:
                    snake.change_direction("RIGHT")

        # Update Snake 
        snake.move()

        # Update AgentBrain
        current_time = pygame.time.get_ticks()

        if current_time - last_enemy_move > Enemy_Move_Delay:###########
            obstacles = snake.body[1:] #################
            
            action = agent.get_action(
                enemy.position,
                snake.body[0],
                obstacles
            )
            if action:
                enemy.move_by_action(action)
        
            last_enemy_move = current_time

        if snake.body[0] == enemy.position:
            running = False
            print("GAME OVER")



        
        if snake.body[0] == food.position:
            score += 1
            snake.grow()
            food.respawn(snake.body, enemy.position)
            

        # Border collision
        head_x, head_y = snake.body[0]
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            running = False

        # Self collision
        if snake.body[0] in snake.body[1:]:
            running = False

        # Draw everything

        window.fill(BLACK)

        pygame.draw.rect(window, WHITE, (0, 0, WINDOW_WIDTH, SCORE_BAR_HEIGHT))
        score_text = font.render(f"Score: {score} High Score: {highscore}", True, BLACK)
        window.blit(score_text, (10, 10))
        
        

        snake.draw(window, SCORE_BAR_HEIGHT)
        food.draw(window)
        enemy.draw(window, SCORE_BAR_HEIGHT)

        pygame.display.update()
        clock.tick(SNAKE_SPEED)
        
        if score > highscore:
            save_highscore(score)
            highscore = score
        

    pygame.quit()
    print("Game Over! Final Score:", score)


if __name__ == "__main__":
    main()
