import tkinter as tk
from tkinter import messagebox
class Validation(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("600x800")
        self.title("Gestionnaire de taches")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        frame = tk.Frame(self)
        frame.grid(row=0, column=0, sticky="ewsn")
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=10)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=5)
        frame.rowconfigure(4, weight=5)
        frame.rowconfigure(5, weight=5)
        frame.rowconfigure(6, weight=10)
        frame.rowconfigure(7, weight=40)
        vcmd = (self.register(self.valider_entree), '%P')
        invcmd = (self.register(self.entree_invalide),)

        tk.Label(frame, text="Ma To-Do List", font=("Arial", 25), fg="black").grid(row=0, column=0, columnspan=2,sticky="ew",padx=10, pady=10)

        tk.Label(frame, text="Taper la tâche à ajouter:", font=("Arial", 10), fg="black").grid(row=1, column=0, sticky="w", padx=15,pady=10)
        self.entree1 = tk.Entry(frame)
        self.entree1.grid(row=1, column=1, sticky="ew",padx=10,pady=10)

        tk.Label(frame, text="Durée estimeée de la tache en minutes:", font=("Arial", 10), fg="black").grid(row=2, column=0,sticky="w", padx=15,pady=10)
        self.entree2 = tk.Entry(frame,validate='key',validatecommand=vcmd,invalidcommand=invcmd)
        self.entree2.grid(row=2, column=1, sticky="ew",padx=10,pady=10)

        self.prioriteres = tk.BooleanVar(value=True)
        self.boutton1 = tk.Checkbutton(frame, text="Toutes les nouvelles tâches sont prioritere", variable=self.prioriteres)
        self.boutton1.grid(row=3, column=0,columnspan=2, sticky="w",padx=15)

        tk.Label(frame, text="Choisir le type de tâche:", font=("Arial", 10), fg="black").grid(row=4,column=0, rowspan=2,sticky="w",padx=15)
        self.radio = tk.StringVar(value="Personnel")
        self.rb1 = tk.Radiobutton(frame, text="Personnel", variable=self.radio, value="Personnel")
        self.rb2 = tk.Radiobutton(frame, text="Professionel", variable=self.radio, value="Professionel")
        self.rb1.grid(row=4, column=1, sticky="w")
        self.rb2.grid(row=5, column=1, sticky="w")

        self.bouton= tk.Button(frame, text="Ajouter la tache", font=("Arial", 9), command=self.entree_tache, state= "disabled")
        self.bouton.grid(row=6, column=0, sticky="ew", columnspan=2, padx=250,pady=20)

        self.list = tk.Listbox(frame, width=55, height=11, relief="ridge", bd=2)
        self.list.grid(row=7, column=0, columnspan=2, sticky="nsew")


    def valider_entree(self, nouvelle_valeur):
        self.bouton_tache()
        if nouvelle_valeur == "":
            return True
        try:
            valeur = int(nouvelle_valeur)
            if 1 <= valeur <= 480:
                return True
            else:
                raise ValueError("La valeur doit être entre 1 et 480.")
        except ValueError:
            return False


    def entree_invalide(self):
        messagebox.showwarning("Entrée invalide", "Veuillez entrer un entier (positif).")

    def entree_tache(self):
        entre = self.entree1.get()
        nombre = self.entree2.get()
        radio = self.radio.get()
        if entre.strip() != "" and nombre.strip() != "":
            if self.prioriteres.get():
                self.list.insert(tk.END, f"[P][{radio}][{nombre}][{entre}]")
            else:
                self.list.insert(tk.END, f"[{radio}][{nombre}][{entre}]")
            self.entree1.delete(0, tk.END)
            self.entree2.delete(0, tk.END)
        else:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")

    def bouton_tache(self):
        if 0 < (len(self.entree1.get())) and 0 < (len(self.entree2.get())):
            self.bouton.config(state="active")
        else:
            self.bouton.config(state="disabled")






if __name__ == "__main__":
    Validation().mainloop()