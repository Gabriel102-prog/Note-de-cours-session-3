import tkinter as tk
from tkinter import ttk as ttk

class Compte(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulateur de compte")
        self.geometry("800x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        # Frame 1
        self.frame1 = ttk.Frame(self)
        self.frame1.grid(row=0, column=0, sticky="nsew",padx=10, pady=10)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)
        self.frame1.rowconfigure(1, weight=1)
        self.frame1.columnconfigure(2, weight=1)
        self.frame1.rowconfigure(2, weight=1)
        self.frame1 = ttk.LabelFrame(self.frame, text="Données du compte")
        self.label1.grid(row=0, column=0, sticky="snew") #TODO
        self.label2 = ttk.Label(self.label1, text="Numéro", font=("Arial", 10))
        self.label2.grid(row=0, column=0, sticky="ew", padx=10)
        self.label3 = ttk.Label(self.frame1, text="Détenteur", font=("Arial", 10))
        self.label3.grid(row=1, column=0, sticky="ew", padx=10)
        self.label4 = ttk.Label(self.frame1, text="Solde", font=("Arial", 10))
        self.label4.grid(row=2, column=0, sticky="ew", padx=10)
        self.entry1 = ttk.Entry(self.frame1, font=("Arial", 10))
        self.entry1.grid(row=0, column=1, sticky="ew", padx=10)
        self.checkbutton1 = ttk.Checkbutton(self.frame1, text="Gelé")
        self.checkbutton1.grid(row=0, column=2, sticky="ew", padx=10)
        self.entry2 = ttk.Entry(self.frame1, font=("Arial", 10))
        self.entry2.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10)
        self.entry3 = ttk.Entry(self.frame1, font=("Arial", 10))
        self.entry3.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10)


        # Frame2
        self.frame2 = ttk.Frame(self)
        self.frame2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.rowconfigure(2, weight=1)
        self.label2 = ttk.LabelFrame(self.frame2, text="Montant")
        self.label2.grid(row=0, column=0, sticky="ew")
        self.entry4 = ttk.Entry(self.frame2, font=("Arial", 10))
        self.entry4.grid(row=0, column=0, sticky="ew")




        #Frame 3
        self.frame3 = ttk.Frame(self)
        self.frame3.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.rowconfigure(0, weight=1)
        self.frame3.columnconfigure(1, weight=1)
        self.frame3.columnconfigure(2, weight=1)
        self.frame3.columnconfigure(3, weight=1)
        self.bt6 = ttk.Button(self.frame3, text="Déposer")
        self.bt6.grid(row=0, column=0, padx=10, pady=10)
        self.bt7 = ttk.Button(self.frame3, text="Retirer")
        self.bt7.grid(row=0, column=1, padx=10, pady=10)
        self.bt8 = ttk.Button(self.frame3, text="Vider")
        self.bt8.grid(row=0, column=2, padx=10, pady=10)
        self.bt9 = ttk.Button(self.frame3, text="Reset")
        self.bt9.grid(row=0, column=3, padx=10, pady=10)





if __name__ == "__main__":
    Compte().mainloop()
