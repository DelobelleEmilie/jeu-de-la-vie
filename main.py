import tkinter as tk
from random import randrange
from tkinter import messagebox
import time
import random


class Cellule:
    #valeur vrai faux
    alive: bool
    #valeur entier
    age: int

    def __init__(self, alive: bool, age: int):
        self.alive = alive  # "Vivante" ou "Morte"
        self.age = age

    def __str__(self):
        alive = ("Vivante", "Morte")[self.alive]
        return f"[{alive} - {self.age}]"

    #gérer quand la cellule est morte
    #ajout d'âge
    def add_age(self, value: int):
        if self.age < 1:
            self.age += 1
            return

        self.age += value

        if self.age >= 10:
            # age négatif parce qu'on doit compter 5 tours avant de la faire renaitre
            self.age = -5
            self.alive = False

    #fonction naissance
    def born(self):
        self.age = 1
        self.alive = True

    #fonction obtention d'âge
    def get_age(self):
        return self.age

    #fonction de vie
    def is_alive(self):
        return self.alive


#damier
class GameBoard:
    size: int
    cellules: []

    def __init__(self, size: int, ratio: float):
        self.size = size
        self.cellules = []
        for x in range(self.size):
            self.cellules.append([])
            for y in range(self.size):
                #la vie est random entre le radio - 1
                alive = random.random() > (1 - ratio)
                #enregistre les valeurs dans un tableau
                self.cellules[x].append(Cellule(alive, (1, 0)[alive]))

    #chere la taille du tableau
    def print(self):
        alive = 0
        dead = 0
        for x in range(self.size):
            for y in range(self.size):
                cell: Cellule = self.cellules[x][y]
                print(f"({x},{y}) - {cell}")
                if (cell.alive):
                    alive += 1
                else:
                    dead += 1
        print(f"{alive} vivantes et {dead} mortes")



# On crée la fenêtre principale
root = tk.Tk()
root.title("Jeu de la vie")
root.geometry("500x500")

board = GameBoard(10, 0.4)
board.print()

# Create an image object using the PhotoImage class
image = tk.PhotoImage(file="background.png")
# Create a label and set the image as its background
label = tk.Label(root, image=image)
# Add the label to the window and use the place layout manager
# to position it at the center of the window
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# button = tk.Button(root, text="Démarrer le jeu", command=plateauJeu)
# button.pack()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Redémarrer la partie", )
filemenu.add_command(label="Quitter la partie", command=exit)
filemenu.add_separator()
filemenu.add_command(label="Exit", )
menubar.add_cascade(label="File", )
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Régles", )
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
root.mainloop()
