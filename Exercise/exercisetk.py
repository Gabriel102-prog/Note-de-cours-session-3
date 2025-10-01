import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface simple")
        self.geometry("400x600")
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.label1 = tk.Label(self.frame, text="Nombre 1", font=("Arial", 20))
        self.entry1 = tk.Entry(self.frame, width=25)
        self.label2 = tk.Label(self.frame, text="Nombre 2", font=("Arial", 20))
        self.entry2 = tk.Entry(self.frame, width=25)
        self.bouton1 = tk.Button(self.frame, text="Adittion", command=self.calculer)
        self.bouton2 = tk.Button(self.frame, text="Multiplication", command=self.calculer2)
        self.label1.pack(padx=10, pady=10)
        self.entry1.pack(padx=10, pady=10)
        self.label2.pack(padx=10, pady=10)
        self.entry2.pack(padx=10, pady=10)
        self.bouton1.pack(padx=10, pady=10)
        self.bouton2.pack(padx=10, pady=10)

    def calculer(self):
        valeur1_str = self.entry1.get().strip()
        valeur2_str = self.entry2.get().strip()

        if valeur1_str == "" or valeur2_str == "":
            messagebox.showerror("Erreur", "Veuillez entrer une valeur dans les deux champs.")
            return

        try:
            valeur1 = int(valeur1_str)
            valeur2 = int(valeur2_str)
            resultat = valeur1 + valeur2
            messagebox.showinfo("Résultat", f"Le résultat est : {resultat}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

    def calculer2(self):
        valeur1_str = self.entry1.get().strip()
        valeur2_str = self.entry2.get().strip()

        if valeur1_str == "" or valeur2_str == "":
            messagebox.showerror("Erreur", "Veuillez entrer une valeur dans les deux champs.")
            return

        try:
            valeur1 = int(valeur1_str)
            valeur2 = int(valeur2_str)
            resultat = valeur1 * valeur2
            messagebox.showinfo("Résultat", f"Le résultat est : {resultat}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

if __name__ == "__main__":
    app = App()
    app.mainloop()


class Email(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("800x100")
        self.create_widgets()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


    def create_widgets(self):
        frame = tk.Frame(self)
        frame.grid(row=0, column=0, sticky="ew")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(1, weight=40)
        frame.columnconfigure(2, weight=1)


        tk.Label(frame, text="Nom:", font=("Arial", 10), fg="black").grid(row=0, column=0, sticky="e",padx=5, pady=5)
        entre1 = tk.Entry(frame)
        entre1.grid(row=0, column=1, sticky="ew",padx=5, pady=5)

        tk.Label(frame, text="Email:", font=("Arial", 10), fg="black").grid(row=1, column=0, sticky="we",padx=5, pady=5)
        entre2 = tk.Entry(frame)
        entre2.grid(row=1, column=1, sticky="ew",padx=5, pady=5)


        tk.Button(frame, text="Valider").grid(row=0, column=2,rowspan= 2, sticky="w",padx=5, pady=5)



if __name__ == "__main__":
    Email().mainloop()
