import tkinter as tk

class Fenetre1(tk.Tk):
    def __init__(self):
        super().__init__()

        # Chargement de l'image en arrière-plan
        image = tk.PhotoImage(file="background.png")

        # Ajout de l'image en tant qu'arrière-plan
        canvas = tk.Canvas(self, width=200, height=100)
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        canvas.pack()

        # Ajout d'un bouton pour ouvrir la fenêtre 2
        bouton = tk.Button(self, text="Ouvrir fenêtre 2", command=self.ouvrir_fenetre2)
        bouton.pack()

        # Ajout de texte
        label = tk.Label(self, text="Fenêtre 1")
        label.pack()
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Redémarrer la partie", command=restart)
        filemenu.add_command(label="Quitter la partie", command=exit)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", )
        menubar.add_cascade(label="File", )
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Régles", command=regles)
        menubar.add_cascade(label="Help", menu=helpmenu)

        pausemenu = tk.Menu(menubar, tearoff=0)
        pausemenu.add_command(label="Pause", command=pause)
        menubar.add_cascade(label="Pause", menu=helpmenu)

class Fenetre2(tk.Tk):
    def __init__(self):
        super().__init__()

        # Chargement de l'image en arrière-plan
        image = tk.PhotoImage(file="background2.png")

        # Ajout de l'image en tant qu'arrière-plan
        canvas = tk.Canvas(self, width=200, height=100)
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        canvazss.pack()

        # Ajout d'un bouton pour ouvrir la fenêtre 3
        bouton = tk.Button(self, text="Ouvrir fenêtre 3", command=self.ouvrir_fenetre3)
        bouton.pack()

        # Ajout de texte
        label = tk.Label(self, text="Le jeu se déroule dans une grille à deux dimensions composée de cellules qui peuvent être vivantes  ou mortes. /n Chaque cellule a huit cellules voisines adjacentes (horizontalement, verticalement et diagonalement) et un âge compris entre 1 et 10.À chaque itération, l'état de chaque cellule est déterminé par l'état de ses cellules voisines et de son âge selon les règles suivantes (dans cet ordre de priorité):La cellule gagne 1 an.La cellule gagne 1 an supplémentaire par cellule voisine vivante (par exemple, si elle a 3 cellules voisines vivantes, elle gagne 1 an supplémentaire).Si la cellule a plus de 10 ans, elle meurt et ne peut pas devenir vivante à l'itération suivante. /n Si la cellule est morte et possède au moins trois cellules voisines vivantes, elle devient vivante avec un âge de 1 an. /n Si la cellule est morte pendant 5 itérations, elle redevient vivante.L'interface graphique utilise les couleurs suivantes pour indiquer l'âge de chaque cellule: bleu pour 4 à 8 ans, jaune pour 1 à 3 ans, rouge pour plus de 9 ans.Lors du lancement de l'application, l'utilisateur peut choisir la taille de la grille (qui doit être un carré avec au moins 10 cases sur un côté). 40% des cellules de la grille sont initialisées comme vivantes.")
        label.pack()
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Redémarrer la partie", command=restart)
        filemenu.add_command(label="Quitter la partie", command=exit)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", )
        menubar.add_cascade(label="File", )
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Régles", command=regles)
        menubar.add_cascade(label="Help", menu=helpmenu)

        pausemenu = tk.Menu(menubar, tearoff=0)
        pausemenu.add_command(label="Pause", command=pause)
        menubar.add_cascade(label="Pause", menu=helpmenu)

class Fenetre3(tk.Tk):
    def __init__(self):
        super().__init__()


        # Ajout de texte
        label = tk.Label(self, text="Fenêtre 3")
        label.pack()
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Redémarrer la partie", command=restart)
        filemenu.add_command(label="Quitter la partie", command=exit)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", )
        menubar.add_cascade(label="File", )
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Régles", command=regles)
        menubar.add_cascade(label="Help", menu=helpmenu)

        pausemenu = tk.Menu(menubar, tearoff=0)
        pausemenu.add_command(label="Pause", command=pause)
        menubar.add_cascade(label="Pause", menu=helpmenu)

        for ligne in range(8):
            for colonne in range(8):
                x1 = colonne * taille_case
                y1 = ligne * taille_case
                x2 = x1 + taille_case
                y2 = y1 + taille_case
                couleur = "white"
                if (ligne + colonne) % 2 == 0:
                    couleur = "black"
                canvas.create_rectangle(x1, y1, x2, y2, fill=couleur)


fenetre1 = Fenetre1()
fenetre1.mainloop()
