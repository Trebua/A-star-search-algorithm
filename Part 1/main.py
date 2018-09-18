from astar import astar
from cell import Cell
from board import Board

def main():
    bpath = "board-1-1.txt"
    board = Board(bpath)
    print(board)
    a = astar(board)
    print(a)

main()