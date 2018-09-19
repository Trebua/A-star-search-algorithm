from astar import astar
from cell import Cell
from board import Board

def main():
    bpath = "board-1-2.txt"
    board = Board(bpath)
    a = astar(board)
    s = board.path_repr(a)
    print(a)
    board.board_image(a)
    print(s)


main()