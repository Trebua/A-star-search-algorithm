from astar import astar
from bfs import bfs
from dijkstra import dijkstra
from cell import Cell
from board import Board

def main():
    bpath = "board-2-4.txt"
    board = Board(bpath)
    b, o, c = dijkstra(board)
    board.board_to_image_e(b,o,c)
    print("Opened: " + str(len(o)))
    print("Closed: " + str(len(c)))

main()