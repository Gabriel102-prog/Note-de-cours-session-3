import tkinter as tk
from tkinter import ttk
class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion  de stock")
        self.geometry("900x500")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=1)


        self.frame1 = ttk.LabelFrame(self, text="Fiche article")
        self.frame1.grid(column=0, row=0, sticky="snew")
        self.frame1.rowconfigure((0,1,2,3,4), weight=1)
        self.frame1.rowconfigure(5, weight=2)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)

        self.label1 = ttk.Label(self.frame1, text="Statut:")
        self.label1.grid(row=0, column=0,sticky="ew")
        self.variable1 = tk.StringVar()
        self.variable1.set("Achat")
        self.values1 = ["Vendue", "Acheté"]
        self.list1 = ttk.Combobox(self.frame1, values=self.values1, state="readonly", textvariable=self.variable1)
        self.list1.grid(row=0, column=1,sticky="ew")
        self.list1.bind("<<ComboboxSelected>>", self.statut)

        self.label2 = ttk.Label(self.frame1, text="ISBN:")
        self.label2.grid(row=1, column=0,sticky="ew")
        self.entry2 = ttk.Entry(self.frame1, width=10)
        self.entry2.grid(row=1, column=1,sticky="ew")

        self.label3 = ttk.Label(self.frame1, text="Titre:")
        self.label3.grid(row=2, column=0,sticky="ew")
        self.entry3 = ttk.Entry(self.frame1, width=10)
        self.entry3.grid(row=2, column=1,sticky="ew")

        self.label4 = ttk.Label(self.frame1, text="Auteur:")
        self.label4.grid(row=3, column=0,sticky="ew")
        self.entry4 = ttk.Entry(self.frame1, width=10)
        self.entry4.grid(row=3, column=1,sticky="ew")

        self.label_achete = ttk.Label(self.frame1, text="Quantité Acheté:")
        self.label_achete.grid(row=4, column=0,sticky="ew")
        self.entry_achete = ttk.Entry(self.frame1, width=10)
        self.entry_achete.grid(row=4, column=1,sticky="ew")
        self.label_vendue = ttk.Label(self.frame1, text="Quantité vendue:")
        self.label_vendue.grid(row=4, column=0,sticky="ew")

        self.frame12 = ttk.LabelFrame(self.frame1, text="Outil de gestion")
        self.frame12.grid(row=5, column=0, columnspan=2, sticky="snew")
        self.frame12.columnconfigure((0, 1), weight=1)
        self.frame12.rowconfigure((0, 1), weight=1)

        self.bt_achete = ttk.Button(self.frame12, text="Ajouter")
        self.bt_achete.grid(column=0, row=0, sticky="ew")
        self.bt_vendue = ttk.Button(self.frame12, text="Vendue")
        self.bt2 = ttk.Button(self.frame12, text="Supprimer")
        self.bt2.grid(column=0, row=1, sticky="ew")
        self.bt3 = ttk.Button(self.frame12, text="Modifier")
        self.bt3.grid(column=1, row=0, sticky="ew")
        self.bt4 = ttk.Button(self.frame12, text="Quitter")
        self.bt4.grid(column=1, row=1, sticky="ew")





        self.frame2 = ttk.Frame(self)
        self.frame2.grid(column=1, row=0, sticky="snew")
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.tree = ttk.Treeview(self.frame2, columns=["ID", "ISBN", "Titre", "Auteur", "Quantité en stock"], show="headings", selectmode="extended")
        self.tree.heading("Titre", text="Titre")
        self.tree.heading("Auteur", text="Auteur")
        self.tree.heading("ISBN", text="ISBN")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Quantité en stock", text= "Quantité en stock")
        self.tree.column("ID", width=50)
        self.tree.column("ISBN", width=75)
        self.tree.column("Titre", width=75, anchor="center")
        self.tree.column("Auteur", width=75)
        self.tree.column("Quantité en stock", width=150)
        self.tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


    def statut(self, event = None):
        if self.variable1.get() == "Achat":
            self.label_achete.grid()
            self.bt_achete.grid()
            self.bt_vendue.grid_remove()
            self.label_vendue.grid_remove()
        else:
            self.label_achete.grid_remove()
            self.bt_achete.grid_remove()
            self.bt_vendue.grid()
            self.label_vendue.grid()


            # self.label5_2 = ttk.Label(self.frame1, text="Quantité acheté")
            # self.label5_2.grid(row=4, column=0,sticky="ew")
            # self.bt1.grid_remove()
            # self.bt1_2 = ttk.Button(self.frame1, text="Acheté")
            # self.bt1_2.grid(column=0, row=0, sticky="ew")
        if self.variable1.get() == "Enprunté":
            self.label5.grid_remove()

if __name__ == "__main__":
    Interface().mainloop()