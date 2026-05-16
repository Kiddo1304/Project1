import pygame
from settings import *

class Enemy:
    def __init__(self):
        #initialising enemy position on the grid
        self.position = [1, 1]

    def move_to(self, pos):
        #directly update the enemy position
        self.position = list(pos)

    def move_by_action(self, action):
        #extract current position
        x, y = self.position

#update position of the enemy based on action space
        if action == "UP":
            y -= 1
        elif action == "DOWN":
            y += 1
        elif action == "LEFT":
            x -= 1
        elif action == "RIGHT":
            x += 1

        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            self.position = [x,y]

    def draw(self, surface, offset):
        #render the enemy
        pygame.draw.rect(
            surface, WHITE,
            (self.position[0] * CELL_SIZE,
             self.position[1] * CELL_SIZE + offset,
            CELL_SIZE, CELL_SIZE)
        )