import tkinter as tk
from tkinter import ttk as ttk
import random
from tkinter import messagebox


class Compte(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulateur de compte---Gabriel Bertrand")
        self.geometry("900x300")
        self.columnconfigure(0, weight=2)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.utilisateur = {}

        # Frame 1
        self.frame1 = ttk.LabelFrame(self, text="Données du compte")
        self.frame1.grid(row=0, column=0, sticky="nsew",padx=10, pady=10)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=5)
        self.frame1.rowconfigure(1, weight=1)
        self.frame1.columnconfigure(2, weight=1)
        self.frame1.rowconfigure(2, weight=1)
        self.label2 = ttk.Label(self.frame1, text="Numéro:", font=("Arial", 10))
        self.label2.grid(row=0, column=0, sticky="e")
        self.label3 = ttk.Label(self.frame1, text="Détenteur:", font=("Arial", 10))
        self.label3.grid(row=1, column=0, sticky="e")
        self.label4 = ttk.Label(self.frame1, text="Solde:", font=("Arial", 10))
        self.label4.grid(row=2, column=0, sticky="e")
        self.entry1 = ttk.Entry(self.frame1,font=("Arial", 10))
        self.entry1.grid(row=0, column=1, sticky="ew", padx=10)
        self.gele = tk.BooleanVar(value=False)
        self.checkbutton1 = ttk.Checkbutton(self.frame1, text="Gelé", variable=self.gele, command=self.geler)
        self.checkbutton1.grid(row=0, column=2, padx=10)
        self.entry2 = ttk.Entry(self.frame1, font=("Arial", 10))
        self.entry2.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10)
        self.entry3 = ttk.Entry(self.frame1, font=("Arial", 10),state="readonly")
        self.entry3.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10)


        # Frame2
        self.frame2 = ttk.LabelFrame(self, text="Montant")
        self.frame2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.rowconfigure(2, weight=1)
        self.entry_montant = tk.StringVar()
        self.entry4 = ttk.Entry(self.frame2, textvariable=self.entry_montant, state="readonly", font=("Arial", 10))
        self.entry4.grid(row=0, column=0)
        self.bt1 = ttk.Button(self.frame2, text= "Random", command=self.random,state="active")
        self.bt1.grid(row=1, column=0, padx=10)
        self.valeurs = tk.StringVar(value="")
        self.rad1 = ttk.Radiobutton(self.frame2, text= "1 à 10", variable=self.valeurs, value=[1,10],state="active")
        self.rad1.grid(row=0, column=1, sticky="ew", padx=10)
        self.rad2 = ttk.Radiobutton(self.frame2, text="10 à 100", variable=self.valeurs, value=[10,100],state="active")
        self.rad2.grid(row=1, column=1, sticky="ew", padx=10)
        self.rad3 = ttk.Radiobutton(self.frame2, text="100 à 1000", variable=self.valeurs, value=[100,1000],state="active")
        self.rad3.grid(row=2, column=1, sticky="ew", padx=10)




        #Frame 3
        self.frame3 = ttk.Frame(self)
        self.frame3.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.rowconfigure(0, weight=1)
        self.frame3.columnconfigure(1, weight=1)
        self.frame3.columnconfigure(2, weight=1)
        self.frame3.columnconfigure(3, weight=1)
        self.bt6 = ttk.Button(self.frame3, text="Déposer", command=self.deposer,state="active")
        self.bt6.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        self.bt7 = ttk.Button(self.frame3, text="Retirer", command= self.retirer,state="active")
        self.bt7.grid(row=0, column=1, sticky="n", padx=10, pady=10)
        self.bt8 = ttk.Button(self.frame3, text="Vider",command=self.vider, state="active")
        self.bt8.grid(row=0, column=2, sticky="n", padx=10, pady=10)
        self.bt9 = ttk.Button(self.frame3, text="Reset", command=self.reset,state="active")
        self.bt9.grid(row=0, column=3, sticky="n", padx=10, pady=10)

    # Fonction pour gén.rer nombre au hazard
    def random(self):
        if self.valeurs.get() == "":
            messagebox.showwarning("Génération de montant impossible", "Veuillez sélectionner un des radio bouton")
            return
        self.entry_montant.set("")
        intervalle = self.valeurs.get()
        liste = list(map(int, intervalle.split()))
        valeur = str(round(random.uniform(liste[0], liste[1]),2))
        self.entry_montant.set(valeur)
    def condition(self):
        if len(self.entry1.get().strip()) != 5 or not self.entry1.get().isdigit():
            messagebox.showwarning("Dépot impossible", "Veuillez entrer un numéro valide d'exactement 5 chiffres.")
            return True
        if len(self.entry2.get().strip()) < 5 or not self.entry2.get().strip().replace(" ", "").isalpha():
            messagebox.showwarning("Dépot impossible", "Veuillez entrer un nom de détenteur valide d'au moins 5 caractères.")
            return True
        if self.entry4.get() == "":
            messagebox.showwarning("Dépot impossible", "Veuillez faire générer un montant random")
            return True

    def deposer(self):
        clé = (self.entry1.get(), self.entry2.get().strip())
        num1, det1 = clé
        if self.condition():
            return
        for clés in self.utilisateur:
            num2, det2 = clés
            if num1 == num2 and det1 != det2:
                messagebox.showwarning("Dépot impossible","Le numéro de compte que vous avez rentré existe déja. Veuillez le changer.")
                return
        if clé in self.utilisateur:
            depot = float(self.entry4.get())
            montant_initial = self.utilisateur[clé]
            self.entry3.config(state="normal")
            self.entry3.delete(0, "end")
            self.entry3.insert("end", str(round(depot + montant_initial, 2)))
            self.entry3.config(state="readonly")
            self.utilisateur[clé] += depot

        if not clé in self.utilisateur:
            depot = float(self.entry4.get())
            self.entry3.config(state="normal")
            self.entry3.delete(0, "end")
            self.entry3.insert(0, str(round(depot, 2)))
            self.entry3.config(state="readonly")
            self.utilisateur[self.entry1.get(), self.entry2.get().strip()] = depot

    def retirer(self):
        clé = (self.entry1.get(), self.entry2.get().strip())
        if self.condition():
            return
        if not clé in self.utilisateur:
            messagebox.showwarning("Compte introuvable", "Veuillez vous créé un compte en déposant un montant")
            return
        if clé in self.utilisateur:
            retrait = float(self.entry4.get())
            montant_initial = self.utilisateur[clé]
            if (montant_initial - retrait) < 0:
                messagebox.showwarning("Fonds insufisant", "Vous n'avez pas assez dans votre compte pour retirer ce montant")
                return
            self.entry3.config(state="normal")
            self.entry3.delete(0, "end")
            self.entry3.insert("end", str(round(montant_initial - retrait, 2)))
            self.entry3.config(state="readonly")
            self.utilisateur[clé] -= retrait

    def reset(self):
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.entry3.config(state= "normal")
        self.entry3.delete(0, "end")
        self.entry3.config(state="readonly")
        self.entry_montant.set("")
        self.valeurs.set("")
        self.gele.set(False)

    def vider(self):
        clé = (self.entry1.get(), self.entry2.get().strip())
        self.utilisateur[clé] = 0
        self.entry3.config(state="normal")
        self.entry3.delete(0, "end")
        self.entry3.insert(0,"0")
        self.entry3.config(state="readonly")

    def geler(self):
        if self.gele.get():
            self.bt1.config(state="disabled")
            self.bt6.config(state="disabled")
            self.bt7.config(state="disabled")
            self.bt8.config(state="disabled")
            self.bt9.config(state="disabled")
            self.rad1.config(state="disabled")
            self.rad2.config(state="disabled")
            self.rad3.config(state="disabled")
            self.entry1.config(state="disabled")
            self.entry2.config(state="disabled")
            self.entry3.config(state="disabled")
            self.entry4.config(state="disabled")
        else:
            self.bt1.config(state="normal")
            self.bt6.config(state="normal")
            self.bt7.config(state="normal")
            self.bt8.config(state="active")
            self.bt9.config(state="active")
            self.rad1.config(state="active")
            self.rad2.config(state="active")
            self.rad3.config(state="active")
            self.entry1.config(state="normal")
            self.entry2.config(state="normal")
            self.entry3.config(state="normal")
            self.entry4.config(state="normal")



if __name__ == "__main__":
    Compte().mainloop()
