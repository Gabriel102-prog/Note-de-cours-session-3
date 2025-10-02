import tkinter as tk
from tkinter import ttk as ttk


class Formulaire(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Formulaire")
        self.geometry("800x600")
        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)

        # 1 Frame
        self.frame.columnconfigure(0, weight=2)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=12)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=2)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=2)
        self.label1 = ttk.Label(self.frame, text="Nom", font=("Arial", 10))
        self.label1.grid(row=0, column=0, sticky="w", padx=10)
        self.label2 = ttk.Label(self.frame, text="Email", font=("Arial", 10))
        self.label2.grid(row=0, column=1, sticky="w", padx=10)
        self.label3 = ttk.Label(self.frame, text="Âge", font=("Arial", 10))
        self.label3.grid(row=0, column=2, sticky="w", padx=10)
        self.entry1 = ttk.Entry(self.frame)
        self.entry1.grid(row=1, column=0, sticky="ew", padx=10)
        self.entry2 = ttk.Entry(self.frame)
        self.entry2.grid(row=1, column=1, sticky="ew", padx=10)
        self.entry3 = ttk.Entry(self.frame)
        self.entry3.grid(row=1, column=2, sticky="ew", padx=10)
        self.bout1 = ttk.Button(self.frame, text="Ajouter")
        self.bout1.grid(row=1, column=3, sticky="ew", padx=10)
        self.bout2 = ttk.Button(self.frame, text="Supprimer sélection")
        self.bout2.grid(row=1, column=4, sticky="ew", padx=10)
        # Frame2
        self.frame2 = ttk.Frame(self)
        self.frame2.grid(row=1, column=0, sticky="nsew")
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.list = ttk.Treeview(self.frame2, columns=("Nom", "Email", "Âge"), show="headings")
        self.list.heading("Nom", text="Nom")
        self.list.heading("Email", text="Email")
        self.list.heading("Âge", text="Âge")
        self.list.column("Nom", width=150)
        self.list.column("Email", width=200)
        self.list.column("Âge", width=50, anchor="center")
        self.list.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        #Frame3
        self.frame3 = ttk.Frame(self)
        self.frame3.grid(row=2, column=0, sticky="nsew")
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.rowconfigure(0, weight=1)
        self.frame3.columnconfigure(1, weight=1)
        self.frame3.columnconfigure(2, weight=10)
        self.frame3.columnconfigure(3, weight=1)
        self.frame3.columnconfigure(4, weight=1)
        self.bout3 = ttk.Button(self.frame3, text="Import JSON")
        self.bout3.grid(row=0, column=0, sticky="ew" )
        self.bout4 = ttk.Button(self.frame3, text="Import CSV")
        self.bout4.grid(row=0, column=1, sticky="ew")
        self.bout5 = ttk.Button(self.frame3, text="Import Json")
        self.bout5.grid(row=0, column=3, sticky="ew")
        self.bout6 = ttk.Button(self.frame3, text="Exporter CSV")
        self.bout6.grid(row=0, column=4, sticky="ew")


if __name__ == "__main__":
    Formulaire().mainloop()


