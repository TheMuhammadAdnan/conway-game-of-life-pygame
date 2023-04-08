import random
import pygame
import sys
from pygame.locals import *


class Node:
    def __init__(self, row, column, state):
        self.row = row
        self.column = column
        self.state = state
        self.neighbors = []
        self.next_state = 0

    def display(self, window):
        if self.state == 1:
            pygame.draw.rect(window, (255, 255, 255), (self.column * 10, self.row * 20, 20, 20))
        else:
            pygame.draw.rect(window, (0, 0, 0), (self.column * 20, self.row * 20, 20, 20))
    
    def update(self):
        self.state = self.next_state
    
    def find_neighbors(self, grid):
        self.neighbors = grid.find_neighbors(self)
    
    def check_state(self):
        alive = 0
        for neighbor in self.neighbors:
            if neighbor.state == 1:
                alive += 1
        if self.state == 1:
            if alive < 2:
                self.next_state = 0
            elif alive > 3:
                self.next_state = 0
            else:
                self.next_state = 1
        else:
            if alive == 3:
                self.next_state = 1
            else:
                self.next_state = 0


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Node(y, x, 0) for x in range(columns)] for y in range(rows)]
        # initialize pygame
        pygame.init()

        # set up the window
        self.window = pygame.display.set_mode((1600, 900), 0, 32)

    def find_neighbors(self, node):
        neighbors = []
        for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            row = node.row + i
            col = node.column + j
            if row >= 0 and row < self.rows and col >= 0 and col < self.columns:
                neighbors.append(self.grid[row][col])
        return neighbors
    
    # display 2d array on pygame window
    def display(self):
        for row in self.grid:
            for node in row:
                node.display(self.window)
    
    def randomlife(self):
        for row in self.grid:
            for node in row:
                node.state = random.randint(0, 1)


def main():
    grid = Grid(90, 160)
    grid.randomlife()

    for row in grid.grid:
        for node in row:
            node.find_neighbors(grid)
    
    delay = 100

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for row in grid.grid:
            for node in row:
                node.check_state()

        for row in grid.grid:
            for node in row:
                node.update()

        grid.display()
        pygame.display.update()
        pygame.time.delay(delay)


if __name__ == "__main__":
    main()
