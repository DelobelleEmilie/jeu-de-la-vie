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

    def __init__(self,create):
        self.window = tk.Tk()
        self.scrollbar = tk.Scale(self.window , from_=10, to=None, orient=tk.HORIZONTAL, resolution=10)
        self.scrollbar.pack()
        self.btn = self.Button(self.win, text="Valider", command=create)
        self.btn.pack(pady=10)

    # Créer un bouton pour valider la valeur de la barre de défilement
    def validate(self):
        self.value = self.scrollbar.get()
        self.board = GameBoard( self.value, 0.4)
        # Lancer une autre page ou exécuter une autre fonction ici en utilisant la valeur
    def create(self):
        self.win = GameWindow(self.board)
        self.value = self.scale.get()

class menubar():
    def __init__(self):
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(menubar, tearoff=0)
        self.filemenu.add_command(label="Redémarrer la partie", command=self.restart)
        self.filemenu.add_command(label="Quitter la partie", command=exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", )
        self.menubar.add_cascade(label="File", )
        self.helpmenu = tk.Menu(menubar, tearoff=0)
        self.helpmenu.add_command(label="Régles", command=self.regles)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.pausemenu = tk.Menu(menubar, tearoff=0)
        self.pausemenu.add_command(label="Pause", command=self.pause)
        self.menubar.add_cascade(label="Pause", menu=self.helpmenu)
        self.root.config(menu=menubar)
