import tkinter as tk

from logique import GameBoard


class menubar():
    def __init__(self,start,pause):

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
        self.control_menu = tk.Menu(menubar)

        self.menu_bar.add_cascade(label='Control', menu=self.control_menu)
        self.pause_button = tk.MenuButton(self.control_menu, label='Pause', command=pause)
        self.control_menu.add_command(label='Pause', command=pause)

        self.control_menu.add_command(label='Start', command=start)
        self.root.config(menu=menubar)

    def start(self):
        # réactivez le bouton pause ici
        self.pause_button.configure(state='normal')

    def pause(self):
        # désactivez le bouton pause ici
        self.pause_button.configure(state='disabled')

    def on_mouse_click(self,event):
        # vérifiez si le bouton pause est enfoncé ici
        if self.pause_button .is_pressed():
            self.pause()
            # changez l'état de la cellule ici
            self.cell.state = not self.cell.state










