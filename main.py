from astar import astar
from cell import Cell
from board import Board

def main():
    bpath = "board-1-2.txt"
    board = Board(bpath)
    a = astar(board)
    board.board_image(a)


main()