# Import module
from tkinter import *

# Create object
root = Tk()
page1 = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage(file="background.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

label2 = Label(root, text="Welcome")
label2.pack(pady=50)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady=20)


def create():
    win = Toplevel(root)


verifierBouton = Button(root, text="Commencer le jeu", command=create)
verifierBouton.pack(anchor=CENTER)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Rédemarrer la partie", )

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Execute tkinter
root.mainloop()