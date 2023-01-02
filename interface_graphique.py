import tkinter as tk

from logique import GameBoard

class GameWindow:

    root : tk.Tk
    board: GameBoard
    canvas: tk.Canvas

    def __init__(self, board: GameBoard):
        self.board = board
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        self.draw()
        self.root.mainloop()
        self.root.after(1000, self.loop)
        self.root.mainloop()

    def draw(self):
        cell_size = 800 / self.board.size
        for x in range(self.board.size):
            for y in range(self.board.size):
                x1 = x * cell_size
                y1 = y * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.board.cellules[x][y].get_color())

    def loop(self):
        self.board.update()
        self.draw()
        self.root.after(1000, self.loop)