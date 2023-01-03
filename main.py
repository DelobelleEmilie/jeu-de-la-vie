from interface_graphique import GameWindow
from interface_graphique import SlideBar
from logique import Cellule, GameBoard

board = GameBoard(value, 0.4)
board.print()

win = SlideBar()
win = GameWindow(board)