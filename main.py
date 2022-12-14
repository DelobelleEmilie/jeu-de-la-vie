import tkinter as tk
from random import randrange
from tkinter import messagebox
import time
import random

class Cellule:
    def __init__(self, etat, age):
        self.etat = etat # "Vivante" ou "Morte"
        self.age = random.randint(1, 10)
        self.nouvel_etat = self.etat
    def update(self, self.etat):
    if etat > 0 :
        etat = self.etat += 1

    elif etat > 10 :
        print("La cellule est morte")
    else:
        etat = self.etat += 1



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


button = tk.Button(root, text="Démarrer le jeu", command=plateauJeu)
button.pack()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Redémarrer la partie", )
filemenu.add_command(label="Quitter la partie",command=exit )
filemenu.add_separator()
filemenu.add_command(label="Exit", )
menubar.add_cascade(label="File", )
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Régles", )
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
root.mainloop()
