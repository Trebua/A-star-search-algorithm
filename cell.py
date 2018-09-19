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
        self.g = self.cost #kanskje 0?
        self.h = 0
        self.f = 0
        self.opened = False
        self.closed = False
    
    def get_path_cost(self,c):
        costs = {".": 1, "#": inf, "A": 1, "B": 1, "w": 100, "m": 50, "f": 10, "g": 5, "r": 1}
        return costs[c]

    def __str__(self):
        return self.c

    def add_adjacent(self, cell):
        self.adjacent.append(cell)

    def get_adjacents(self):
        return self.adjacent

    def get_color(self, c):
        dict = {".": (255,255,255), "#": (0,0,0), "A": (221, 255, 216), "B": (221, 255, 216), "w": (0,0,255), "m": (153,153,153), "f": (2, 102, 33), "g": (83, 232, 129), "r": (163, 130, 99)}
        dicthex = {".": "white", "#": "black", "A": "red", "B": "red", "w": "blue", "m": "gray", "f":"#044400", "g": "#0de500", "r": "#c9a380"}
        return dicthex[c]

    def set_parent(self, cell):
        self.best_parent = cell

    def calculate_h(self, board):
        goal = board.goal_coords
        coords = self.coords
        self.h = abs(goal[0] - coords[0]) + abs(goal[1] - coords[1])
        return self.h
