import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import json

class Produit:
    def __init__(self, name, quantity, price):
        self.nom = name
        self.quantite = quantity
        self.prix = price

    @property
    def nom(self):
        return self.__name

    @nom.setter
    def nom(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le nom du produit doit Ãªtre une chaÃ®ne non vide.")
        self.__name = value.strip()

    @property
    def quantite(self):
        return self.__quantity

    @quantite.setter
    def quantite(self, value):
        s = str(value).strip()
        if not s.isdigit():
            raise ValueError("La quantitÃ© doit Ãªtre un entier positif (0 inclus).")
        iv = int(s)
        if iv < 0:
            raise ValueError("La quantitÃ© ne peut pas Ãªtre nÃ©gative.")
        self.__quantity = iv

    @property
    def prix(self):
        return self.__price

    @prix.setter
    def prix(self, value):
        try:
            val = float(value)
        except Exception:
            raise ValueError("Le prix doit Ãªtre un nombre.")
        if val < 0:
            raise ValueError("Le prix ne peut pas Ãªtre nÃ©gatif.")
        self.__price = val

    def to_dict(self):
        return {"name": self.nom, "quantity": self.quantite, "price": self.prix}

class ProductManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("gestion des produits")
        self.create_widgets()

    def create_widgets(self):
        self.head_frame = tk.LabelFrame(self, text="Ajouter un produit", padx=10, pady=10)
        self.head_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.head_frame.columnconfigure(1, weight=1)

        #labels
        lbl_produit = tk.Label(self.head_frame, text="Produit:")
        lbl_produit .grid(row=0, column=0, sticky="e", padx=5, pady=2)

        lbl_quantite = tk.Label(self.head_frame, text="QuantitÃ©:")
        lbl_quantite.grid(row=1, column=0, sticky="e", padx=5, pady=2)

        lbl_prix = tk.Label(self.head_frame, text="Prix:")
        lbl_prix.grid(row=2, column=0, sticky="e", padx=5, pady=2)

        #inputs
        self.entry_name = tk.Entry(self.head_frame)
        self.entry_name.grid(row=0, column=1, columnspan=2, padx=5, pady=2, sticky="we")

        self.entry_quantity = tk.Entry(self.head_frame)
        self.entry_quantity.grid(row=1, column=1, padx=5, pady=2, sticky="we")

        self.entry_price = tk.Entry(self.head_frame)
        self.entry_price.grid(row=2, column=1, padx=5, pady=2, sticky="we")

        #bouton
        self.btn_add = tk.Button(self.head_frame, text="Ajouter Produit", command=self.ajouter_produit)
        self.btn_add.grid(row=0, column=3, rowspan=3, padx=10, pady=2, sticky="we")

        self.frame_manage = tk.LabelFrame(self, text="Gestion des produits", padx=10, pady=10)
        self.frame_manage.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.frame_manage.columnconfigure((0, 1, 2, 3), weight=1)

        self.btn_delete = tk.Button(self.frame_manage, text="Supprimer Produit", command=self.supprimer_produit)
        self.btn_delete.grid(row=0, column=0, columnspan=2, pady=5)

        self.btn_update = tk.Button(self.frame_manage, text="Modifier Produit", command=self.modifier_produit)
        self.btn_update.grid(row=0, column=2, columnspan=2, pady=5)

        self.btn_save_csv = tk.Button(self.frame_manage, text="Sauvegarder CSV", command=self.sauvegarder_csv)
        self.btn_save_csv.grid(row=1, column=0, padx=5, pady=10)

        self.btn_save_json = tk.Button(self.frame_manage, text="Sauvegarder JSON", command=self.sauvegarder_json)
        self.btn_save_json.grid(row=1, column=1, padx=5, pady=10)

        self.btn_load_csv = tk.Button(self.frame_manage, text="Importer CSV", command=self.importer_csv)
        self.btn_load_csv.grid(row=1, column=2, padx=5, pady=10)

        self.btn_load_json = tk.Button(self.frame_manage, text="Importer JSON", command=self.importer_json)
        self.btn_load_json.grid(row=1, column=3, padx=5, pady=10)

        self.columns = ("name", "quantity", "price")
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")
        self.tree.heading("name", text="Produit")
        self.tree.heading("quantity", text="QuantitÃ©")
        self.tree.heading("price", text="Prix")
        self.tree.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(2, weight=1)

    def ajouter_produit(self):
        nom = self.entry_name.get()
        quantite = self.entry_quantity.get()
        prix = self.entry_price.get()
        try:
            produit = Produit(nom, quantite, prix)
            self.tree.insert("", "end", values=(produit.nom, produit.quantite, produit.prix))
            self.entry_name.delete(0, "end")
            self.entry_quantity.delete(0, "end")
            self.entry_price.delete(0, "end")
        except ValueError as e:
            messagebox.showerror("Erreur de saisie", str(e))

    def supprimer_produit(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("SÃ©lection requise", "Veuillez sÃ©lectionner un produit Ã  supprimer.")
            return
        for item in selected:
            self.tree.delete(item)

    def modifier_produit(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("SÃ©lection requise", "Veuillez sÃ©lectionner un produit Ã  modifier.")
            return

        item = selected[0]
        values = self.tree.item(item, "values")
        # self.entry_name.delete(0, tk.END)
        # self.entry_quantity.delete(0, tk.END)
        # self.entry_price.delete(0, tk.END)

        self.entry_name.insert(0, values[0])
        self.entry_quantity.insert(0, values[1])
        self.entry_price.insert(0, values[2])

        self.tree.delete(item)

    def sauvegarder_csv(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not filepath:
            return
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(self.columns)
            for row in self.tree.get_children():
                writer.writerow(self.tree.item(row)["values"])
        messagebox.showinfo("SuccÃ¨s", "Produits sauvegardÃ©s en CSV.")

    def sauvegarder_json(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not filepath:
            return
        data = []
        for row in self.tree.get_children():
            data.append(dict(zip(self.columns, self.tree.item(row)["values"])))
        with open(filepath, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("SuccÃ¨s", "Produits sauvegardÃ©s en JSON.")

    def importer_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not filepath:
            return

        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                produit = Produit(row["name"], row["quantity"], row["price"])
                self.tree.insert("", "end", values=(produit.nom, produit.quantite, produit.prix))

        messagebox.showinfo("Import CSV terminÃ©",f"ligne(s) importÃ©e(s).")

    def importer_json(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not filepath:
            return

        with open(filepath, mode='r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            messagebox.showerror("Erreur JSON", "Le fichier JSON doit contenir une liste d'objets.")
            return

        for item in data:
            produit = Produit(item["name"], item["quantity"], item["price"])
            self.tree.insert("", "end", values=(produit.nom, produit.quantite, produit.prix))

        messagebox.showinfo("Import JSON terminÃ©"," Ã©lÃ©ment(s) importÃ©(s)")


if __name__ == "__main__":
    app = ProductManagerApp()
    app.mainloop()