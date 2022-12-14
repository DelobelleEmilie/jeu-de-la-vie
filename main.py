from tkinter import *
from tkinter.ttk import *

#On crée la fenêtre principale
root = Tk()

root.title("Jeu de la vie")

frame = Frame(root)
button = Button(frame, text='Voulez vous lancer une partie?')

#On agence le widget avec une méthode de géométrie dans la Frame
button.pack()
#On enclenche la boucle Main
root.mainloop()