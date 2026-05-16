from settings import *
import pygame

class Snake:
    def __init__(self):
        #snake starting in the middle
        self.body = [
            [GRID_WIDTH // 2, GRID_HEIGHT // 2],
            [GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2],
            [GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2]
        ]
        self.direction = "RIGHT"
        self.next_direction = self.direction

    def change_direction(self, new_dir):
        #defining opposite directions to prevent invalid movement
        opposite = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }
        if new_dir != opposite[self.direction]:
            self.next_direction = new_dir

    def move(self):
        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        
# snake movement
        if self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1
        elif self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1

        new_head = [head_x, head_y]
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        #increase snake length
        tail = self.body[-1]
        self.body.append(tail.copy())

    def draw(self, surface, offset_y): 
        #render snake
        for block in self.body:
            pygame.draw.rect(
                surface, RED,
                (block[0] * CELL_SIZE,
                 block[1] * CELL_SIZE + offset_y,
                CELL_SIZE, CELL_SIZE)
    )