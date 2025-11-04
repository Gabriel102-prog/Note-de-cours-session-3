import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class Sqlite(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRUD Example")
        self.geometry("750x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=6)
        self.nb_ajouter = 0
        self.init_db()


        self.frame1 = ttk.LabelFrame(self, text="Fiche")
        self.frame1.grid(column=0, row=0, padx=10, pady=10, sticky="snew")
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=10)
        self.frame1.columnconfigure(2, weight=1)
        self.frame1.columnconfigure(3, weight=10)
        self.frame1.columnconfigure(4, weight=1)
        self.frame1.columnconfigure(5, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=1)

        self.label1 = ttk.Label(self.frame1, text="Nom")
        self.label1.grid(column=0, row=0, padx=10, pady=10)
        self.entry1 = ttk.Entry(self.frame1)
        self.entry1.grid(column=1, row=0, padx=10, pady=10, sticky="ew")
        self.label2 = ttk.Label(self.frame1, text="Email")
        self.label2.grid(column=2, row=0, padx=10, pady=10)
        self.entry2 = ttk.Entry(self.frame1)
        self.entry2.grid(column=3, row=0, padx=10, pady=10, sticky="ew")
        self.label3 = ttk.Label(self.frame1, text="Âge")
        self.label3.grid(column=4, row=0, padx=10, pady=10)
        self.entry3 = ttk.Entry(self.frame1)
        self.entry3.grid(column=5, row=0, padx=10, pady=10, sticky="ew")

        self.frame2 = ttk.Frame(self.frame1)
        self.frame2.grid(column=0, row=1,columnspan=6, padx=10, pady=10, sticky="snew")
        self.frame2.columnconfigure((0,1,2,3), weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.bt1 = ttk.Button(self.frame2, text="Nouveau", command=self.nouveau)
        self.bt1.grid(column=0, row=0, padx=10, pady=10, sticky="ew")
        self.bt2 = ttk.Button(self.frame2, text="Ajouter", command=self.ajouter)
        self.bt2.grid(column=1, row=0, padx=10, pady=10, sticky="ew")
        self.bt3 = ttk.Button(self.frame2, text="Modifier")
        self.bt3.grid(column=2, row=0, padx=10, pady=10, sticky="ew")
        self.bt4 = ttk.Button(self.frame2, text="Supprimer")
        self.bt4.grid(column=3, row=0, padx=10, pady=10, sticky="ew")

        self.tree = ttk.Treeview(self,columns=("ID", "Nom", "Email", "Âge"), show="headings", selectmode="extended")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Âge", text="Âge")
        self.tree.column("ID", width=10)
        self.tree.column("Nom", width=50)
        self.tree.column("Email", width=70)
        self.tree.column("Âge", width=10)
        self.tree.grid(column=0, row=2, columnspan=6, padx=10,pady= 10, sticky="snew")
        self.tree.bind("<<TreeviewSelect>>", self.selectionner)

    def init_db(self):
        self.conn = sqlite3.connect("people.db")
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS people
                       (
                           id    INTEGER PRIMARY KEY AUTOINCREMENT,
                           name  TEXT,
                           age   INTEGER,
                           email TEXT    NOT NULL,
                           age   INTEGER NOT NULL
                       )""")
        self.conn.commit()

    def _insert(self, name, age, email):
        self.conn.execute("INSERT INTO people(name, age, email) VALUES (?, ?, ?)", (name, age, email))
        self.conn.commit()

    def _updapte(self, name, age, email):
        self.conn.execute("UPDATE people SET name = ?, age = ? WHERE email = ?", (name, age, email))
        self.conn.commit()

    def _delete(self, row_id):
        self.conn.execute("DELETE FROM people WHERE id = ?", row_id)
        self.conn.commit()

    def _fetch_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, email, age, email FROM people ORDER BY id DESC")
        return cur.fetchall()


    def selectionner(self, event):
        selection = self.tree.selection()
        if selection:
            valeurs = self.tree.item(selection[0], "values")
            id, nom, email, age = valeurs
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
            self.entry3.delete(0, tk.END)
            self.entry1.insert(0, nom)
            self.entry2.insert(0, email)
            self.entry3.insert(0, age)

    def ajouter(self):
        self._validate()
        self.nb_ajouter += 1
        self.tree.insert("", "end", values=(self.nb_ajouter, self.entry1.get(),self.entry2.get(),self.entry3.get()))
        messagebox.showinfo("Ajout avec succes", "Ajout avec succes")
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.entry3.delete(0, "end")

    def nouveau(self):
        self.tree.delete(*self.tree.get_children())

    def _validate(self):
        name = self.entry1.get()
        age = self.entry2.get()
        email = self.entry3.get()
        if not name or not email or not age:
            messagebox.showwarning("Erreur",  "tous les champs sont obligatoire")
            return
        if not age.isdigit():
            messagebox.showwarning("Erreur", "tous les champs obligatoire")
            return
        return name, email, int(age)
    def _clear_form(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
    def _load_road(self):
        for item  in self.tree.get_children():
            self.tree.delete(item)
        for row in self._fetch_all():
            self.tree.insert("", "end", values=row)
    def _update_button(self):
        pass
        # selection = self.selected_id is not None
        #
        # self.btn_ed


if __name__ == "__main__":
    app = Sqlite()
    app.mainloop()