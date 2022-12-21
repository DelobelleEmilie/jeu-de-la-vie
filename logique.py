import tkinter as tk
from random import randrange
from tkinter import messagebox
import time
import random

paused = False


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
                # (1 -=bool (si ratio = 0.4, 40% de chance d'être True) ratio)
                #alive = variable
                #random.random = nombre entre 0 et 1
                alive = random.random() > \(1 - ratio)
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

def create():
    win = Toplevel(root)

def AjoutCase():
    for x in range(self.size):
        for y in range(self.size):
            voisines_vivantes = 0;
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if i >= 0 and i < size and j >= 0 and j < sizeand (i != 0 or j != 0):
                        if grid[i][j].is_alive():
                            voisines_vivantes += 1
            age = 1;
            if voisines_vivantes > 2:
                age += voisines_vivantes - 2;
            grid[x][y].add_age(age)



def Couleur():
    if cell.years > 9:
        # La cellule est âgée de plus de 9 ans, couleur rouge
        color = "red"
    elif cell.years > 3:
        # La cellule est âgée entre 4 et 8 ans, couleur bleue
        color = "blue"
    elif cell.years > 0:
        # La cellule est âgée entre 1 et 3 ans, couleur jaune
        color = "yellow"
    else:
        # La cellule est âgée de moins de 1 an, couleur par défaut
        color = "default"


def Pause():
    global paused
    paused = True

def Unpause():
    global paused
    paused = False

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()
canvas.create_carre(x, x,command = couleur, fill="red")