import tkinter as tk

class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.nb_time_not_work = 0
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
            self.nb_time_not_work += 1
            if self.nb_time_not_work > 3:
                self.entre.delete(0, "end")
                self.entre.insert("end", "Putain,apprend à calculer")
                raise ValueError("erreur")
            else:
                self.entre.delete(0, "end")
                self.entre.insert("end","Erreur")
                raise ValueError("erreur")


if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()



class Dolist(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de tâches")
        self.geometry("600x750")
        self.create_widgets()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.grid(row=0, column=0, sticky="ewsn")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=5)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(4, weight=5)
        frame.rowconfigure(5, weight=1)
        frame.rowconfigure(6, weight=1)
        frame.rowconfigure(7, weight=1)
        frame.rowconfigure(8, weight=1)
        frame.rowconfigure(9, weight=5)

        tk.Label(frame, text="Ma To-Do List", font=("Arial",25), fg="black").grid(row=1, column=0, sticky="ewsn", padx=80, pady=10)
        tk.Entry(frame, relief="ridge", bd=5).grid(row=2, column=0, sticky="ewsn",padx=150)

        tk.Button(frame, text="Ajouter la tache", font=("Arial",9)).grid(row=3, column=0, sticky="ewsn", padx=250,pady=10 )

        tk.Listbox(frame, width=55, height=11, relief="ridge", bd=5).grid(row=4, column=0, sticky="ew", padx=100)

        prioriteres = tk.BooleanVar(value=True)
        tk.Checkbutton(frame,text="Toutes les taches sont prioritere",variable=prioriteres).grid(row=5, column=0, sticky="ewsn")

        radio = tk.StringVar(value="Personnel")
        rb1 = tk.Radiobutton(frame, text="Personnel", variable=radio, value="Personnel")
        rb21 = tk.Radiobutton(frame, text="Professionel", variable=radio, value="Professionel")
        rb1.grid(row=6, column=0, sticky="ewsn")
        rb21.grid(row=7, column=0, sticky="ewsn")

        label_notes = tk.Label(frame, text="Notes sur taches sélectionnée:", font=("Arial",10), fg="black")
        label_notes.grid(row=8, column=0, sticky="ewsn")

        tk.Text(frame, width=50, height=10, relief="ridge", bd=5).grid(row=9, column=0, sticky="ewsn",padx= 100)


if __name__ == "__main__":
    Dolist().mainloop()
