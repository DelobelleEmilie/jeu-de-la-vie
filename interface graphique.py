import tkinter as tk

# Créez la fenêtre principale
window = tk.Tk()

# Créez les widgets Frame pour chaque page
frame1 = tk.Frame(window, bg="white")
frame2 = tk.Frame(window, bg="white")
frame3 = tk.Frame(window, bg="white")

# Ajoutez des widgets de texte au widget Frame de chaque page
label1 = tk.Label(frame1, text="Page 1")
label1.pack()

label2 = tk.Label(frame2, text="Page 2")
label2.pack()

label3 = tk.Label(frame3, text="Page 3")
label3.pack()

# Créez une fonction de rappel pour chaque bouton qui affichera la page souhaitée
def show_frame1():
    frame1.pack(fill="both", expand=True)
    frame2.pack_forget()
    frame3.pack_forget()

def show_frame2():
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)
    frame3.pack_forget()

def show_frame3():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)

# Créez les boutons pour passer d'une page à l'autre
button1 = tk.Button(frame1, text="Page 2", command=show_frame2)
button1.pack()

button2 = tk.Button(frame2, text="Page 3", command=show_frame3)
button2.pack()

button3 = tk.Button(frame3, text="Page 1", command=show_frame1)
button3.pack()

# Affichez la première page au démarrage
show_frame1()

# Démarrez la boucle d'événements Tkinter
window.mainloop()
