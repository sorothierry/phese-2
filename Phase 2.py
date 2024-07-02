

import tkinter as tk
from tkinter import messagebox

# Créer la fenêtre Tkinter
root = tk.Tk()
root.title("TIC-TAC-TOE")

# Définir la liste des chiffres de 1 à 9
chiffres = list(range(1, 10))

# Initialiser la variable mark
mark = ''

# Initialiser la variable count
count = 0

# Créer la liste panels avec 10 éléments
panels = ['panel'] + list(range(1, 10))

def verification(chiffre):
    global count, mark, chiffres

    if chiffre in chiffres:
        chiffres.remove(chiffre)
        count += 1

        if count % 2 == 0:
            mark = 'O'
        else:
            mark = 'X'

        if chiffre == 1:
            bouton1.config(text=mark)
        elif chiffre == 2:
            bouton2.config(text=mark)
        elif chiffre == 3:
            bouton3.config(text=mark)
        elif chiffre == 4:
            bouton4.config(text=mark)
        elif chiffre == 5:
            bouton5.config(text=mark)
        elif chiffre == 6:
            bouton6.config(text=mark)
        elif chiffre == 7:
            bouton7.config(text=mark)
        elif chiffre == 8:
            bouton8.config(text=mark)
        elif chiffre == 9:
            bouton9.config(text=mark)

        if victoire():
            if mark == 'X':
                messagebox.showinfo("Félicitations!", "Joueur1 à gagné")
            else:
                messagebox.showinfo("Félicitations!", "Joueur2 à gagné")
            root.destroy()
        elif count > 8:
            messagebox.showinfo("Égalité", "Match à égalité")
            root.destroy()
    else:
        messagebox.showerror("Erreur", "Position déjà prise ou invalide")

def victoire():
    # Les combinaisons gagnantes
    combinaisons = [
        [bouton1, bouton2, bouton3],
        [bouton4, bouton5, bouton6],
        [bouton7, bouton8, bouton9],
        [bouton1, bouton4, bouton7],
        [bouton2, bouton5, bouton8],
        [bouton3, bouton6, bouton9],
        [bouton1, bouton5, bouton9],
        [bouton3, bouton5, bouton7]
    ]

    for combinaison in combinaisons:
        if combinaison[0]["text"] == combinaison[1]["text"] == combinaison[2]["text"] != "":
            return True
    return False

# Création des boutons
bouton1 = tk.Button(root, text="", font=('normal', 20), width=5, height=2,fg="red", command=lambda: verification(1))
bouton1.grid(row=1, column=0)

bouton2 = tk.Button(root, text="", font=('normal', 20), width=5, height=2, command=lambda: verification(2))
bouton2.grid(row=1, column=1)

bouton3 = tk.Button(root, text="", font=('normal', 20), width=5, height=2,fg="red", command=lambda: verification(3))
bouton3.grid(row=1, column=2)

bouton4 = tk.Button(root, text="", font=('normal', 20), width=5, height=2, command=lambda: verification(4))
bouton4.grid(row=2, column=0)

bouton5 = tk.Button(root, text="", font=('normal', 20), width=5, height=2,fg="red", command=lambda: verification(5))
bouton5.grid(row=2, column=1)

bouton6 = tk.Button(root, text="", font=('normal', 20), width=5, height=2, command=lambda: verification(6))
bouton6.grid(row=2, column=2)

bouton7 = tk.Button(root, text="", font=('normal', 20), width=5, height=2,fg="red", command=lambda: verification(7))
bouton7.grid(row=3, column=0)

bouton8 = tk.Button(root, text="", font=('normal', 20), width=5, height=2, command=lambda: verification(8))
bouton8.grid(row=3, column=1)

bouton9 = tk.Button(root, text="", font=('normal', 20), width=5, height=2,fg="red", command=lambda: verification(9))
bouton9.grid(row=3, column=2)

# Afficher la fenêtre Tkinter
root.mainloop()





