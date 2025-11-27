import email
import tkinter as tk
from logging import exception
from tkinter import messagebox
from tkinter import ttk, filedialog
import json, csv
import re

FIELDS = ("nom", "email", "age")


class Formulaire(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("700x450")
        self.init_widgets()
        self.rows = []

    def init_widgets(self):

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        header_content = tk.Frame(self)
        header_content.grid(row=0, column=0, sticky="ew")
        header_content.columnconfigure(0, weight=1)
        header_content.columnconfigure(1, weight=1)
        header_content.columnconfigure(2, weight=1)

        # labels
        self.Nom = tk.Label(header_content, text="Nom")
        self.Nom.grid(row=0, column=0, sticky="w", padx=20, pady=5)
        self.Email = tk.Label(header_content, text="Email")
        self.Email.grid(row=0, column=1, sticky="w", padx=20, pady=5)
        self.Age = tk.Label(header_content, text="Ã‚ge")
        self.Age.grid(row=0, column=2, sticky="w", padx=20, pady=5)

        # inputs
        self.Nom_Entry = tk.Entry(header_content)
        self.Nom_Entry.grid(row=1, column=0, sticky="ew", padx=(20, 5), pady=5)
        self.Email_Entry = tk.Entry(header_content, width=40)
        self.Email_Entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.Age_Entry = tk.Entry(header_content)
        self.Age_Entry.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        # buttons
        self.Btn_Ajouter = tk.Button(header_content, text="Ajouter", command=self.ajouter)
        self.Btn_Ajouter.grid(row=1, column=3, sticky="e", padx=5, pady=5)
        self.Btn_Supprimer = tk.Button(header_content, text="Supprimer sÃ©lection", command=self.supprimer)
        self.Btn_Supprimer.grid(row=1, column=4, sticky="e", padx=(5, 20), pady=5)

        main_content = tk.Frame(self)
        main_content.grid(row=1, column=0, sticky="snew")
        # Configurer les poids de la grille pour que le Treeview s'Ã©tire bien
        main_content.columnconfigure(0, weight=1)
        main_content.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(main_content, columns=("nom", "email", "age"), show="headings",
                                 selectmode="extended", )
        self.tree.heading("nom", text="Nom")
        self.tree.heading("email", text="Email")
        self.tree.heading("age", text="Ã‚ge")

        self.tree.column("nom", width=200)
        self.tree.column("email", width=380)
        self.tree.column("age", width=80)

        self.tree.grid(row=0, column=0, padx=20, pady=20, sticky="snew")

        footer_content = tk.Frame(self)
        footer_content.grid(row=2, column=0, sticky="snew")
        footer_content.columnconfigure(1, weight=1)
        footer_content.columnconfigure(2, weight=1)
        self.Btn_Importer_Json = tk.Button(footer_content, text="Importer JSON", command=self.importer_json)
        self.Btn_Importer_Json.grid(row=0, column=0, sticky="w", padx=(20, 5), pady=5)
        self.Btn_Importer_CSV = tk.Button(footer_content, text="Importer CSV")
        self.Btn_Importer_CSV.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        self.Btn_Exporter_Json = tk.Button(footer_content, text="Exporter JSON", command=self.exporterJson)
        self.Btn_Exporter_Json.grid(row=0, column=3, sticky="e", padx=5, pady=5)
        self.Btn_Exporter_CSV = tk.Button(footer_content, text="Exporter CSV")
        self.Btn_Exporter_CSV.grid(row=0, column=4, sticky="e", padx=(5, 20), pady=5)

    def ajouter(self):
        nom = self.Nom_Entry.get()
        email = self.Email_Entry.get()
        age = self.Age_Entry.get()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not nom:
            messagebox.showwarning("Validation", "Le nom est requis.")
            return
        if not re.match(pattern, email):
            messagebox.showwarning("Validation", "verifier votre email.")
            return
        if age and not age.isdigit():
            messagebox.showerror("Validation", "Ã‚ge doit Ãªtre un entier.")
            return

        self.tree.insert("", "end", values=(nom, email, age))
        self.rows.append({
            "nom": nom,
            "email": email,
            "age": age
        })
        self.Nom_Entry.delete(0, "end")
        self.Email_Entry.delete(0, "end")
        self.Age_Entry.delete(0, "end")

    def supprimer(self):
        selected_item = self.tree.selection()  # RÃ©cupÃ¨re l'Ã©lÃ©ment sÃ©lectionnÃ©
        if selected_item:
            self.tree.delete(selected_item)  # Supprime l'Ã©lÃ©ment
        else:
            messagebox.showwarning("Avertissement", "Aucun Ã©lÃ©ment sÃ©lectionnÃ©.")


    def exporterJson(self):
        if not self.rows:
            messagebox.showinfo("export json", "Rien Ã  exporter")
            return
        path = filedialog.asksaveasfilename(title="Exporter Json",defaultextension=".json", filetypes=[("Json", "*.json"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.rows, f, indent=4)
            messagebox.showinfo("export json", "Exporter JSON exported.")
        except exception as e:
            messagebox.showerror("echec export json", str(e))

    def importer_json(self):
        path = filedialog.askopenfilename(title="Importer Json", filetypes=[("Json", "*.json"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("le json doit contenir unr liste d'objet")
            self.rows = []
            for r in data:
                if isinstance(r, dict):
                    ligne ={}
                    for k in FIELDS:
                        ligne[k] = r.get(k,"")
                    self.rows.append(ligne)
            self.refresh()
            messagebox.showinfo("importer json", "Importer JSON imported.")
        except exception as e:
            messagebox.showerror("echec importer json", str(e))


    def refresh(self):
        #cette partie est optionnel. si on veux supprimer le contenu du tableau on ajoute cette partie
        # enfants = self.tree.get_children()
        # for item in enfants:
        #     self.tree.delete(item)

        for r in self.rows:
            nom= r.get("nom")
            email= r.get("email")
            age= r.get("age")

            self.tree.insert("", "end", values=(nom, email, age))




if __name__ == "__main__":
    Formulaire().mainloop()