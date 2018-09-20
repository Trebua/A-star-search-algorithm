from astar import astar
from bfs import bfs
from dijkstra import dijkstra
from cell import Cell
from board import Board

def main():
    bpath = "board-2-4.txt"
    board = Board(bpath)
    a = dijkstra(board)
    board.board_to_image(a)

main()