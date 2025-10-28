import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
class Livre:
    def __init__(self, titre, auteur, categorie, statut):
        self.title = titre
        self.auteur = auteur
        self.categorie = categorie
        self.statut = statut

    @property
    def title(self):
        return self.__titre

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le titre doit etre un mot et pas etre vide.")

        self.__titre = value.strip()
    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("L'auteur doit être un mot et pas etre vide.")
        self.__auteur = value.strip()



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de biblihotheque")
        self.geometry("1000x400")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.nouveau = True
        # Première column
        self.frame1 = tk.LabelFrame(self, text="Fiche du livre")
        self.frame1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=2)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=1)
        self.frame1.rowconfigure(2, weight=1)
        self.frame1.rowconfigure(3, weight=1)
        self.frame1.rowconfigure(4, weight=2)

        # Widget frame 1
        self.label1 = tk.Label(self.frame1, text="Titre")
        self.label1.grid(row=0, column=0, sticky="w",padx=5)
        self.label2 = tk.Label(self.frame1, text="Auteur")
        self.label2.grid(row=1, column=0, sticky="w",padx=5)
        self.label3 = tk.Label(self.frame1, text="Catégorie")
        self.label3.grid(row=2, column=0, sticky="w",padx=5)
        self.label4 = tk.Label(self.frame1, text="Statut")
        self.label4.grid(row=3, column=0, sticky="w",padx=5)

        self.entry1 = ttk.Entry(self.frame1)
        self.entry1.grid(row=0, column=1, sticky="ew",padx=10, pady=2)
        self.entry2 = ttk.Entry(self.frame1)
        self.entry2.grid(row=1, column=1, sticky="ew",padx=10, pady=2)
        self.values1 = ["Roman", "essaie", "science","Biographie", "Technologie"]
        self.list1 = ttk.Combobox(self.frame1, values=self.values1, state= "readonly")
        self.list1.grid(row=2, column=1, sticky="ew",padx=10, pady=2)
        self.list2 = ttk.Combobox(self.frame1, values=["Disponible", "Enprunté"], state= "readonly")

        self.list2.grid(row=3, column=1, sticky="ew",padx=10, pady=2)
        #self.list1.bind(, self.)
        #frame/widejet

        self.frame12 = tk.LabelFrame(self.frame1, text="Outil de gestion")
        self.frame12.grid(row=4, column=0,columnspan=2, sticky="nsew",padx=5, pady=5)
        self.frame12.columnconfigure(0, weight=1)
        self.frame12.columnconfigure(1, weight=1)
        self.frame12.columnconfigure(2, weight=1)
        self.frame12.rowconfigure(0, weight=1)
        self.frame12.rowconfigure(1, weight=1)
        #widget de sous-frame
        self.bt1 = ttk.Button(self.frame12, text="Nouveau", command= self.nouveau_produit)
        self.bt1.grid(row=0, column=0, sticky="ew")
        self.bt2 = ttk.Button(self.frame12, text="Ajouter", command= self.ajouter)
        self.bt2.grid(row=0, column=1, sticky="ew")
        self.bt3 = ttk.Button(self.frame12, text="Suprimer", command=self.supprimer_produit)
        self.bt3.grid(row=0, column=2, sticky="ew")
        self.bt4 = ttk.Button(self.frame12, text="Importer JSON", command=self.importer)
        self.bt4.grid(row=1, column=0, sticky="ew")
        self.bt5 = ttk.Button(self.frame12, text="Exporter JSON", command = self.exporter)
        self.bt5.grid(row=1, column=1, sticky="ew")
        self.bt6 = ttk.Button(self.frame12, text="Quitter", command=self.quit)
        self.bt6.grid(row=1, column=2, sticky="ew")


        #Frame 2
        self.frame2 = tk.Frame(self)
        self.frame2.grid(row=0, column=1, sticky="nsew",padx=10, pady=10)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.columns = ("Titre", "Auteur", "Catégorie", "Disponibilité")
        self.tree = ttk.Treeview(self.frame2, columns=self.columns, show="headings", selectmode="extended")
        self.tree.heading("Titre", text="Titre")
        self.tree.heading("Auteur", text="Auteur")
        self.tree.heading("Catégorie", text="Catégorie")
        self.tree.heading("Disponibilité", text="Disponibilité")
        self.tree.column("Titre", width=200)
        self.tree.column("Auteur", width=150, anchor="center")
        self.tree.column("Catégorie", width=100, anchor="center")
        self.tree.column("Disponibilité", width=100)
        self.tree.grid(row=0, column=0, padx=10, sticky="nsew")


    def ajouter(self):
        if not self.list1.get() or  not self.list2.get():
            messagebox.showerror("Erreur",
                                 "Veuillez faire une sélection de catégorie et statut")
            return
        if self.nouveau :
            titre = self.entry1.get()
            auteur = self.entry2.get()
            categorie = self.list1.get()
            statut = self.list2.get()
            try:
                livre = Livre(titre, auteur, categorie, statut)
                self.tree.insert("", "end", values=(livre.title, livre.auteur, livre.categorie, livre.statut))
                self.nouveau = False

            except ValueError as e:
                messagebox.showerror("Erreur de saisie", str(e))
        else:
            messagebox.showerror("Erreur", "Le tableau contient déjà des livres. Cliquez sur /Nouveau/ avant d’ajouter un autre.")
    def supprimer_produit(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Sélection requise", "Veuillez sélectionner un produit à supprimer.")
            return
        for item in selected:
            self.tree.delete(item)


    def nouveau_produit(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.list1.values = None
        self.nouveau = True



    def importer(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not filepath:
            return

        with open(filepath, mode='r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            messagebox.showerror("Erreur JSON", "Le fichier JSON doit contenir une liste d'objets.")
            return

        for item in data:
            livre = Livre(item["Titre"], item["Auteur"], item["Catégorie"], item["Disponibilité"])
            self.tree.insert("", "end", values=(livre.title, livre.auteur, livre.categorie, livre.statut))

        messagebox.showinfo("Import JSON terminé", " Élément(s) importé(s)")


    def exporter(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not filepath:
            return
        data = []
        for row in self.tree.get_children():
            data.append(dict(zip(self.columns, self.tree.item(row)["values"])))
        with open(filepath, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Succès", "Produits sauvegardés en JSON.")



if __name__ == "__main__":
    app = App()
    app.mainloop()