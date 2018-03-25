import string
from tkinter import *

class Plex:

    def GUI(self):
        fenetre = Tk()
        label = Label(fenetre, text="Combien de personnes etudiante ?")
        label.pack()
        entree = Entry(fenetre, textvariable=string, width=30)
        entree.pack()
        fenetre.mainloop()