import tkinter as tk
from random import randrange
from tkinter import messagebox
import time

def plateauJeu():
    # Create a 10x10 grid of labels
    labels = [[tk.Label(root) for _ in range(10)] for _ in range(10)]
    # Add the labels to the grid
    for i in range(10):
        for j in range(10):
            labels[i][j].grid(row=i, column=j)

    # Function to update the grid every second
    def update_grid():
        for i in range(10):
            for j in range(10):
                # Update the text of each label to add 100
                labels[i][j].config(text=int(labels[i][j]["text"]) + 100)
        # Call this function again after 1 second
        root.after(1000, update_grid)
    # Start updating the grid
    update_grid()

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
