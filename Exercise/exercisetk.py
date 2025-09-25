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


class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x500")
        self.frame = tk.Frame(self)
        self.frame.pack(fill="both", expand=True)
        self.entre = tk.Entry(self.frame, width=550, relief="ridge", bd=10, font=("Arial", 25))
        self.entre.pack(fill="both", expand=True)

        self.frame1 = tk.Frame(self.frame)
        self.frame1.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame1, text="C", font=("Arial", 20),background="gray", relief="ridge", bd=3, command=lambda:self.entree("C"))
        self.bouton1.pack(side="left",fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame1, text="/", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("/"))
        self.bouton2.pack(side="left", fill="both", expand=True)
        self.bouton3 = tk.Button(self.frame1, text="*", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("*"))
        self.bouton3.pack(side="left", fill="both", expand=True)

        self.frame2 = tk.Frame(self.frame)
        self.frame2.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame2, text="7", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("7"))
        self.bouton1.pack(side="left", fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame2, text="8", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("8"))
        self.bouton2.pack(side="left", fill="both", expand=True)
        self.bouton3 = tk.Button(self.frame2, text="9", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("9"))
        self.bouton3.pack(side="left", fill="both", expand=True)
        self.bouton4 = tk.Button(self.frame2, text="-", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("-"))
        self.bouton4.pack(side="left", fill="both", expand=True)

        self.frame3 = tk.Frame(self.frame)
        self.frame3.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame3, text="4", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("4"))
        self.bouton1.pack(side="left", fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame3, text="5", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("5"))
        self.bouton2.pack(side="left", fill="both", expand=True)
        self.bouton3 = tk.Button(self.frame3, text="6", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("6"))
        self.bouton3.pack(side="left", fill="both", expand=True)
        self.bouton4 = tk.Button(self.frame3, text="+", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("+"))
        self.bouton4.pack(side="left", fill="both", expand=True)

        self.frame4 = tk.Frame(self.frame)
        self.frame4.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame4, text="1", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("1"))
        self.bouton1.pack(side="left", fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame4, text="2", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("2"))
        self.bouton2.pack(side="left", fill="both", expand=True)
        self.bouton3 = tk.Button(self.frame4, text="3", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("3"))
        self.bouton3.pack(side="left", fill="both", expand=True)
        self.bouton4 = tk.Button(self.frame4, text="=", font=("Arial", 20), relief="ridge", bd=3, command=self.calculer)
        self.bouton4.pack(side="left", fill="both", expand=True)

        self.frame5 = tk.Frame(self.frame)
        self.frame5.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame5, text="0", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("0"))
        self.bouton1.pack(side="left", fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame5, text=".", font=("Arial", 20), relief="ridge", bd=3, command=lambda:self.entree("."))
        self.bouton2.pack(side="left", fill="both", expand=True)


    def entree(self,valeur):
        if valeur == "C":
            self.entre.delete(0, "end")
        if valeur == "/":
            self.entre.insert("end","/")
        if valeur == "*":
            self.entre.insert("end","*")
        if valeur == "+":
            self.entre.insert("end","+")
        if valeur == "-":
            self.entre.insert("end","-")
        if valeur == "1":
            self.entre.insert("end","1")
        if valeur == "2":
            self.entre.insert("end","2")
        if valeur == "3":
            self.entre.insert("end","3")
        if valeur == "4":
            self.entre.insert("end","4")
        if valeur == "5":
            self.entre.insert("end","5")
        if valeur == "6":
            self.entre.insert("end","6")
        if valeur == "7":
            self.entre.insert("end","7")
        if valeur == "8":
            self.entre.insert("end","8")
        if valeur == "9":
            self.entre.insert("end","9")
        if valeur == "0":
            self.entre.insert("end","0")
        if valeur == ".":
            self.entre.insert("end",".")
    def calculer(self):
        calcul = self.entre.get()
        try:
            reponse = str(eval(calcul))
            self.entre.delete(0, "end")
            self.entre.insert("end", reponse)
        except Exception as e:
            self.entre.delete(0, "end")
            self.entre.insert("end","Erreur")
            raise ValueError("erreur")






if __name__ == "__main__":
    app = Calculatrice()
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
