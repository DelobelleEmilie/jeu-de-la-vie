import random


class Cellule:
    # valeur vrai faux
    alive: bool
    # valeur entière
    age: int

    def __init__(self, alive: bool, age: int):
        self.alive = alive  # "Vivante" ou "Morte"
        self.age = age

    def __str__(self):
        alive = ("Vivante", "Morte")[self.alive]
        return f"[{alive} - {self.age}]"

    def update(self):
        # On tue la cellule si elle est trop agée (10 ans).
        if self.age >= 10:
            # age négatif parce qu'on doit compter 5 tours avant de la faire renaitre
            self.age = -5
            self.alive = False

        if self.age > 0 and not self.alive:
            self.born()

    # gérer quand la cellule est morte
    # ajout d'âge
    def add_age(self, value: int):
        if self.age < 1:
            self.age += 1
            return

        self.age += value

    # fonction naissance
    def born(self):
        self.age = 1
        self.alive = True

    # fonction obtention d'âge
    def get_age(self):
        return self.age

    # fonction de vie
    def is_alive(self):
        return self.alive

    def get_color(self):
        if self.age > 9:
            # La cellule est âgée de plus de 9 ans, couleur rouge
            return "red"
        elif self.age > 3:
            # La cellule est âgée entre 4 et 8 ans, couleur bleue
            return "blue"
        elif self.age > 0:
            # La cellule est âgée entre 1 et 3 ans, couleur jaune
            return "yellow"
        else:
            # La cellule est âgée de moins de 1 an, couleur par défaut
            return "white"


# damier
class GameBoard:
    size: int
    cellules: []
    paused: bool

    def __init__(self, size: int, ratio: float):
        self.size = size
        self.cellules = []
        self.paused = False
        for x in range(self.size):
            self.cellules.append([])
            for y in range(self.size):
                # (1 -=bool (si ratio = 0.4, 40% de chance d'être True) ratio)
                # alive = variable
                # random.random = nombre entre 0 et 1.
                alive = random.random() > (1 - ratio)
                # enregistre les valeurs dans un tableau
                self.cellules[x].append(Cellule(alive, (1, 0)[alive]))

    def set_pause(self, paused: bool):
        self.paused = paused

    def update(self):
        for x in range(self.size):
            for y in range(self.size):
                voisines_vivantes = 0
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if 0 <= i < self.size and 0 <= j < self.size and (i != 0 or j != 0):
                            if self.cellules[i][j].is_alive():
                                voisines_vivantes += 1
                age = 1
                if voisines_vivantes > 2:
                    age += voisines_vivantes - 2
                self.cellules[x][y].add_age(age)

        for x in range(self.size):
            for y in range(self.size):
                self.cellules[x][y].update()

    # chere la taille du tableau
    def print(self):
        alive = 0
        dead = 0
        for x in range(self.size):
            for y in range(self.size):
                cell: Cellule = self.cellules[x][y]
                print(f"({x},{y}) - {cell}")
                if cell.is_alive():
                    alive += 1
                else:
                    dead += 1
        print(f"{alive} vivantes et {dead} mortes")