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

class SlideBar():

    def __init__(self):
        self.window = tk.Tk()
        self.scrollbar = tk.Scale(self.window , from_=10, to=None, orient=tk.HORIZONTAL, resolution=10)
        self.scrollbar.pack()

    # Créer un bouton pour valider la valeur de la barre de défilement
    def validate(self):
        value = self.scrollbar.get()
        # Lancer une autre page ou exécuter une autre fonction ici en utilisant la valeur
    def button(self):
        self.button = tk.Button(self.window , text="Valider", command=validate)
        self.button.pack()