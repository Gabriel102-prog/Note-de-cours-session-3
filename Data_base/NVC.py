import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3

class Nvc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Comme tu veux")
        self.geometry("600x400")
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1), weight=1)
        self.init_db()
        self.frame = ttk.LabelFrame(self, text="Info")
        self.frame.grid(column=0, row=0, sticky="SNEW", padx= 10, pady= 10)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=2)
        self.rowconfigure((0,1,2,3), weight=1)

        self.label_capteur = ttk.Label(self.frame, text="Capteur:")
        self.label_capteur.grid(column=0, row=0, sticky="EW")
        self.label_valeur = ttk.Label(self.frame, text="Valeur:")
        self.label_valeur.grid(column=0, row=1, sticky="EW")
        self.label_unite=ttk.Label(self.frame, text="Unite:")
        self.label_unite.grid(column=0, row=2, sticky="EW")

        self.entry_capteur = ttk.Entry(self.frame)
        self.entry_capteur.grid(column=1, row=0, sticky="EW", padx=10)
        self.entry_valeur = ttk.Entry(self.frame)
        self.entry_valeur.grid(column=1, row=1, sticky="EW", padx=10)
        self.valeur = tk.StringVar()
        self.list_unite = ttk.Combobox(self.frame, state="readonly", values=["Cm", "Dm", "Km"], textvariable=self.valeur)
        self.list_unite.grid(column=1, row=2, sticky="EW", padx=10)

        self.bt_enregistrer = ttk.Button(self.frame, text="Enregistrer", command=self.enregistrer)
        self.bt_enregistrer.grid(column=1, row=3)

        self.frame2 = ttk.Frame(self)
        self.frame2.grid(column=0, row=1, sticky="SNEW", padx= 10, pady= 10)
        self.frame2.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.tree = ttk.Treeview(self.frame2, columns=["ID", "Capteur", "Valeur", "Unité"], show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Capteur", text="Capteur")
        self.tree.heading("Valeur", text="Valeur")
        self.tree.heading("Unité", text="Unité")
        self.tree.column("ID", width=25)
        self.tree.column("Capteur", width=50)
        self.tree.column("Valeur", width=50)
        self.tree.column("Unité", width=50)
        self.tree.grid(column=0, row=0, sticky="SNEW")
    def init_db(self):
        self.conn = sqlite3.connect("donnee.db")
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS donnee(id INTEGER PRIMARY KEY AUTOINCREMENT,capteur TEXT NOT NULL,valeur INTEGER NOT NULL,unite TEXT NOT NULL)""")
        self.conn.commit()

    def _insert(self, capteur, valeur, unite):
        self.conn.execute("INSERT INTO donnee(capteur, valeur, unite) VALUES (?, ?, ?)", (capteur, valeur, unite))
        self.conn.commit()

    def _updapte(self,capteur, valeur, unite):
        self.conn.execute("UPDATE donnee SET capteur = ?, valeur = ? WHERE unite = ?", (capteur, valeur, unite))
        self.conn.commit()

    def _delete(self, row_id):
        self.conn.execute("DELETE FROM donnee WHERE id = ?", row_id)
        self.conn.commit()

    def _fetch_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, capteur, valeur, unite FROM donnee ORDER BY id DESC")
        return cur.fetchall()

    def enregistrer(self):
        capteur = self.entry_capteur.get()
        valeur = int(self.entry_valeur.get())
        unite = self.valeur.get()
        self.entry_capteur.delete(0, "end")
        self.entry_valeur.delete(0, "end")
        self.valeur.set("")
        self._insert(capteur, valeur, unite)
        (id1, capteur1, valeur1, unite1) = self._fetch_all()[0]
        self.tree.insert("", "end", values=(id1,capteur1, valeur1, unite1))

if __name__ == "__main__":
    Nvc().mainloop()