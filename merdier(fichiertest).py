import tkinter as tk
from random import randrange
from tkinter import messagebox
import time
import random



class Couleur:
    def __init__(self):
        bleu = (0, 0, 255)
        jaune = (255, 255, 0)
        rouge = (255, 0, 0)

    # Fonction qui retourne la couleur à utiliser en fonction de l'âge de la cellule
    def get_cell_color(self,bleu, rouge, jaune):
        if age >= 9:
            return rouge
        elif age >= 4:
            return bleu
        else:
            return jaune
    def affichage(self):
    # Affichage d'une cellule en utilisant la couleur appropriée
        cell_age = 5
        cell_color = get_cell_color(cell_age)
        draw_cell(cell_color)
class Cellule:
    # Initialisation d'une cellule
    def __init__(self, x, y, etat, age):
        self.x = x
        self.y = y
        self.etat = etat
        self.age = random.randint(1,10)
    # Mise à jour de l'état et de l'âge d'une cellule
    def update(self, voisines_vivantes):
        # Toute cellule vivante gagne 1 an
        if self.etat == 'Vivante':
            self.age += 1

            # Une cellule qui a plus de deux cellules voisines vivantes gagne 1 an supplémentaire par cellule voisine
            if voisines_vivantes > 2:
                self.age += voisines_vivantes - 2

            # Une cellule possédant plus de 10 ans meurt
            if self.age > 10:
                self.etat = 'Morte'
        else:
            # Une cellule morte possédant au moins trois cellules voisines vivantes devient vivante avec un âge de 1 an
            if voisines_vivantes >= 3:
                self.etat = 'Vivante'
                self.age = 1

def ChoixTaille():
    # Demande à l'utilisateur de choisir la taille de la grille
    grid_size = int(input("Choisissez la taille de la grille (minimum 10) : "))
    # Vérifie que la taille choisie est bien supérieure ou égale à 10
    while grid_size < 10:
        print("La taille doit être supérieure ou égale à 10.")
        grid_size = int(input("Choisissez la taille de la grille (minimum 10) : "))

def restart():
    global ChoixTaille
    return ChoixTaille

def regles():
    print("Toute cellule vivante gagne 1 an. \n")
    print(" Une cellule qui a plus de deux cellules voisines vivantes gagne 1 an supplémentaire par cellule voisine. (Si 3 cellules voisines = + 1an, si 4 cellules voisines = + 2 ans, etc …)\n")
    print("Une cellule possédant plus de 10 ans, meurt et ne peut pas être de nouveau vivante durant la prochaine itération.\n")
    print("Une cellule morte possédant au moins trois cellules voisines vivantes devient vivante avec un âge de 1 an.\n")
    print("Une cellule morte pendant cinq itérations redevient vivante\n")

#On crée la fenêtre principale
root = tk.Tk()
root.title("Jeu de la vie")
root.geometry("300x300")

# Create an image object using the PhotoImage class
image = tk.PhotoImage(file="background.png")
# Create a label and set the image as its background
label = tk.Label(root, image=image)
# Add the label to the window and use the place layout manager
# to position it at the center of the window
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


button = tk.Button(root, text="Démarrer le jeu")
button.pack()

label = Label(root, text="Taille du plateau: ")
label.pack(side=RIGHT, padx=5)
verifierBouton = Button(root, text="Valider", command=ChoixTaille)
verifierBouton.pack(side=LEFT, padx=10)
TailleEntry = Entry(root)
TailleEntry.pack(side=LEFT, padx=10 )

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Redémarrer la partie", command=restart )
filemenu.add_command(label="Quitter la partie",command=exit )
filemenu.add_separator()
filemenu.add_command(label="Exit", )
menubar.add_cascade(label="File", )
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Régles", command=regles )
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
root.mainloop()