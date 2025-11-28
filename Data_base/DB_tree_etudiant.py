import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

import pytest

DB_PATH = "people.db"

class GestionEtudiant(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Etudiants")
        self.geometry("700x500")
        self.selected_id = None
        self.widgets()
        self.init_db()
        self._load_rows()
        self._update_buttons()
        self.nb_ajouter = 0

    # ---------- Base de données ----------
    def init_db(self):
        self.conn = sqlite3.connect(DB_PATH)
        cur = self.conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS people(
        id integer PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL ,
        email TEXT NOT NULL,
        age INTEGER NOT NULL
         )
        """)
        self.conn.commit()

    def _insert(self, name, email, age):
        self.conn.execute(
            "INSERT INTO people (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )
        self.conn.commit()

    def _update(self, row_id, name, email, age):
        self.conn.execute(
            "UPDATE people SET name = ?, email = ?, age = ? WHERE id = ?",
            (name, email, age, row_id)
        )
        self.conn.commit()

    def _delete(self, row_id):
        self.conn.execute("DELETE FROM people WHERE id = ?", (row_id,))
        self.conn.commit()

    def _fetch_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, email, age FROM people ORDER BY id DESC")
        return cur.fetchall()

    # ---------- Interface graphique ----------
    def widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Formulaire
        form = ttk.LabelFrame(self, text="Fiche")
        form.grid(row=0, column=0, padx=8, pady=8, sticky="ew")
        for c in range(6):
            form.columnconfigure(c, weight=1 if c in (1, 3) else 0)

        ttk.Label(form, text="Nom").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Email").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Âge").grid(row=0, column=4, padx=6, pady=6, sticky="w")

        self.ent_name = ttk.Entry(form, width=18)
        self.ent_email = ttk.Entry(form, width=24)
        self.ent_age = ttk.Entry(form, width=6)
        self.ent_name.grid(row=0, column=1, padx=6, pady=6, sticky="ew")
        self.ent_email.grid(row=0, column=3, padx=6, pady=6, sticky="ew")
        self.ent_age.grid(row=0, column=5, padx=6, pady=6, sticky="w")

        # Boutons
        btns = ttk.Frame(form)
        btns.grid(row=1, column=0, columnspan=6, sticky="ew", pady=(2, 8))
        for c in range(4):
            btns.columnconfigure(c, weight=1)

        self.btn_new = ttk.Button(btns, text="Nouveau", command=self.ecraser)
        self.btn_add = ttk.Button(btns, text="Ajouter", command=self.ajouter)
        self.btn_edit = ttk.Button(btns, text="Modifier", command=self.modifier)
        self.btn_del = ttk.Button(btns, text="Supprimer", command=self.supprimer)

        self.btn_new.grid(row=0, column=0, padx=4, sticky="ew")
        self.btn_add.grid(row=0, column=1, padx=4, sticky="ew")
        self.btn_edit.grid(row=0, column=2, padx=4, sticky="ew")
        self.btn_del.grid(row=0, column=3, padx=4, sticky="ew")

        # Tableau
        table = ttk.Frame(self)
        table.grid(row=1, column=0, padx=8, pady=(0, 10), sticky="nsew")
        table.columnconfigure(0, weight=1)
        table.rowconfigure(0, weight=1)

        cols = ("id", "name", "email", "age")
        self.tree = ttk.Treeview(table, columns=cols, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.column("id", width=60)
        self.tree.heading("name", text="Nom")
        self.tree.column("name", width=170)
        self.tree.heading("email", text="Email")
        self.tree.column("email", width=280)
        self.tree.heading("age", text="Âge")
        self.tree.column("age", width=60)
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    # ---------- Fonctions utilitaires ----------

    # ---------- Helpers ----------
    def _validate(self):
        name = self.ent_name.get()
        email = self.ent_email.get()
        age_txt = self.ent_age.get()
        if not name or not email or not age_txt:
            messagebox.showwarning("Champs requis", "Completer tous les champs.")
            return None
        if not age_txt.isdigit():
            messagebox.showerror("Age invalide", "L'age doit etre un entier.")
            return None
        return name, email, int(age_txt)

    def _clear_form(self):
        self.ent_name.delete(0, "end")
        self.ent_email.delete(0, "end")
        self.ent_age.delete(0, "end")
        self.ent_name.focus()

    def _load_rows(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in self._fetch_all():
            self.tree.insert("", "end", values=row)

    def _update_buttons(self):
        """Active/désactive les boutons selon la sélection."""
        has_selection = self.selected_id is not None
        # Ajouter toujours actif (si le formulaire est rempli)
        self.btn_edit.state(["!disabled"] if has_selection else ["disabled"])
        self.btn_del.state(["!disabled"] if has_selection else ["disabled"])


    # ---------- Actions principales ----------
    def ecraser(self):
        self._clear_form()
        self.tree.selection_remove(self.tree.selection())
        self.selected_id = None
        self._update_buttons()
        # TODO : effacer la sélection et vider le formulaire


    def ajouter(self):
        if self._validate():
            self._insert(self.ent_name.get(), self.ent_email.get(), self.ent_age.get())
            self._clear_form()
            self._load_rows()
            self.tree.selection_remove(self.tree.selection())
            self.selected_id = None
            self._update_buttons()
            messagebox.showinfo("Ajout avec succes", "Ajout avec succes")
        else:
            return



    def modifier(self):
        selection = self.tree.selection()
        if selection:
            valeur = self.tree.item(selection[0], "values")
            (id,nom,email,age) = valeur
            ids = int(valeur[0])
            if self._validate():
                self._update(ids, self.ent_name.get(), self.ent_email.get(), self.ent_age.get())
                self._load_rows()
        self.selected_id = None
        self._update_buttons()
        # TODO : modifier l’enregistrement sélectionné

    def supprimer(self):
        selection = self.tree.selection()
        if selection:
            if messagebox.askyesno("Supression", "Voulez vous supprimer cette ligne?"):
                item = selection[0]
                valeurs = self.tree.item(item, "values")
                id = int(valeurs[0])
                self.tree.delete(item)
                self._delete(id)
                self._load_rows()
        self.selected_id = None
        self._update_buttons()




    def _on_select(self, _event):
        selection = self.tree.selection()
        if selection:
            valeurs = self.tree.item(selection[0], "values")
            id, nom, email, age = valeurs
            self._clear_form()
            self.ent_name.insert(0, nom)
            self.ent_age.insert(0, age)
            self.ent_email.insert(0, email)
            self.selected_id = int(id)
            self._update_buttons()
        """
            TODO
            Gère la sélection d'une ligne dans le tableau (Treeview).
            - Récupère les valeurs de la ligne sélectionnée.
            - Remplit les champs du formulaire avec ces données pour édition.
            - Met à jour self.selected_id et l'état des boutons (Modifier/Supprimer).

        """


    def destroy(self):
        self.conn.close()
        super().destroy()
        # TODO : fermer proprement la connexion SQLite avant de quitter



if __name__ == "__main__":
    GestionEtudiant().mainloop()
