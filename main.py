from interface_graphique import GameWindow
from interface_graphique import SlideBar
from logique import Cellule, GameBoard

board = GameBoard(10, 0.4)
board.print()

win = GameWindow(board)
win = SlideBar(board)