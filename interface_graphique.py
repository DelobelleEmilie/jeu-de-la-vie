import tkinter as tk

from logique import GameBoard

class SlideBar:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Configuration")
        self.scrollbar = tk.Scale(self.window, from_=10, to=100, orient=tk.HORIZONTAL, resolution=10)
        self.scrollbar.pack()
        self.btn = tk.Button(self.window, text="Valider", command=self.create)
        self.btn.pack(pady=10)
        self.window.mainloop()
    def create(self):
        #recuperer la valeur de la slide bar
        value = self.scrollbar.get()
        # crées la board avec la valeur du slider
        board = GameBoard(int(value), 0.4)
        #envoies la board à la fenetre de jeu
        win = GameWindow(board)

class GameWindow:

    root : tk.Tk
    board: GameBoard
    canvas: tk.Canvas
    speed: float

    def __init__(self, board: GameBoard):
        self.board = board
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Le jeu de la vie")
        self.speed = 1

        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Quitter la partie", command=exit)
        filemenu.add_command(label="Afficher les règles", command=self.rules)
        menubar.add_cascade(label="Fichier", menu=filemenu)
        controlMenu = tk.Menu(menubar, tearoff=0)
        controlMenu.add_command(label="Play", command=self.play)
        controlMenu.add_command(label="Pause", command=self.stop)
        controlMenu.add_command(label="Redémarrer", command=self.restart)
        menubar.add_cascade(label="Controles", menu=controlMenu)
        speedMenu = tk.Menu(menubar, tearoff=0)
        speedMenu.add_command(label="Lent (x0.5)", command=lambda : self.set_speed(0.5))
        speedMenu.add_command(label="Normal", command=lambda : self.set_speed(1))
        speedMenu.add_command(label="Rapide (x2)", command=lambda : self.set_speed(2))
        speedMenu.add_command(label="Très rapide (x4)", command=lambda : self.set_speed(4))
        menubar.add_cascade(label="Vitesse", menu=speedMenu)
        self.root.config(menu=menubar)

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
        if self.board.is_ready:
            self.board.update()
            self.draw()
        self.root.after(int(1000 / self.speed), self.loop)

    def play(self):
        self.board.set_pause(False)

    def stop(self):
        self.board.set_pause(True)

    def restart(self):
        # Reset la partie logique, et draw sera appelée à la fin du traitement
        self.board.reset(self.draw)

    def set_speed(self, value: float):
        self.speed = value

    def rules(self):
        rules = RulesWindow()

class RulesWindow:
    root: tk.Tk

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Règles du jeu")

        rules = "Règles du jeu de la vie ..."
        label = tk.Label(self.root, text=rules)

        label.pack()

        self.root.mainloop()