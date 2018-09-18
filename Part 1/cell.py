from math import *

class Cell:

    def __init__(self, c, i, j):
        self.c = c
        self.cost = self.get_path_cost(c)
        self.color = self.get_color(c)
        self.start = True if c == 'A' else False
        self.stop = True if c == 'B' else False
        self.adjacent = []
        self.best_parent = None
        self.coords = (i,j)
        self.g = 0
        self.h = 0
        self.f = 0
        self.opened = False
        self.closed = False
    
    def get_path_cost(self,c):
        costs = {".": 0, "#": inf, "A": 0, "B": -inf}
        return costs[c]

    def __str__(self):
        return self.c

    def add_adjacent(self, cell):
        self.adjacent.append(cell)

    def get_adjacents(self):
        return self.adjacent

    def get_color(self, c):
        dict = {".": (255,255,255), "#": (0,0,0), "A": (221, 255, 216), "B": (221, 255, 216)}
        return dict[c]

    def set_parent(self, cell):
        self.best_parent = cell

    def calculate_h(self, board):
        goal = board.goal_coords
        coords = self.coords
        return abs(goal[0] - coords[0]) + abs(goal[1] - coords[1])
