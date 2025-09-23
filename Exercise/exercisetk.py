import tkinter as tk
from tkinter import messagebox
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Interface simple")
#         self.geometry("400x600")
#         self.frame = tk.Frame(self)
#         self.frame.pack()
#         self.label1 = tk.Label(self.frame, text="Nombre 1", font=("Arial", 20))
#         self.entry1 = tk.Entry(self.frame, width=25)
#         self.label2 = tk.Label(self.frame, text="Nombre 2", font=("Arial", 20))
#         self.entry2 = tk.Entry(self.frame, width=25)
#         self.bouton1 = tk.Button(self.frame, text="Adittion", command=self.calculer)
#         self.bouton2 = tk.Button(self.frame, text="Multiplication", command=self.calculer2)
#         self.label1.pack(padx=10, pady=10)
#         self.entry1.pack(padx=10, pady=10)
#         self.label2.pack(padx=10, pady=10)
#         self.entry2.pack(padx=10, pady=10)
#         self.bouton1.pack(padx=10, pady=10)
#         self.bouton2.pack(padx=10, pady=10)
#
#     def calculer(self):
#         valeur1_str = self.entry1.get().strip()
#         valeur2_str = self.entry2.get().strip()
#
#         if valeur1_str == "" or valeur2_str == "":
#             messagebox.showerror("Erreur", "Veuillez entrer une valeur dans les deux champs.")
#             return
#
#         try:
#             valeur1 = int(valeur1_str)
#             valeur2 = int(valeur2_str)
#             resultat = valeur1 + valeur2
#             messagebox.showinfo("Résultat", f"Le résultat est : {resultat}")
#         except ValueError:
#             messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")
#
#     def calculer2(self):
#         valeur1_str = self.entry1.get().strip()
#         valeur2_str = self.entry2.get().strip()
#
#         if valeur1_str == "" or valeur2_str == "":
#             messagebox.showerror("Erreur", "Veuillez entrer une valeur dans les deux champs.")
#             return
#
#         try:
#             valeur1 = int(valeur1_str)
#             valeur2 = int(valeur2_str)
#             resultat = valeur1 * valeur2
#             messagebox.showinfo("Résultat", f"Le résultat est : {resultat}")
#         except ValueError:
#             messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("600x400")
        self.frame = tk.Frame(self)
        self.frame.pack(fill="both", expand=True)
        self.entre = tk.Entry(self.frame, width=550, relief="ridge")
        self.entre.pack(padx=10, pady=10, fill="both", expand=True)

        self.frame1 = tk.Frame(self.frame)
        self.frame1.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame1, text="C", font=("Arial", 20))
        self.bouton1.pack(padx=5, pady=5, side="left",fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame1, text="/", font=("Arial", 20))
        self.bouton2.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton3 = tk.Button(self.frame1, text="*", font=("Arial", 20))
        self.bouton3.pack(padx=5, pady=5, side="left", fill="both", expand=True)

        self.frame2 = tk.Frame(self.frame)
        self.frame2.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame2, text="7", font=("Arial", 20))
        self.bouton1.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame2, text="8", font=("Arial", 20))
        self.bouton2.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton3 = tk.Button(self.frame2, text="9", font=("Arial", 20))
        self.bouton3.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton4 = tk.Button(self.frame2, text="-", font=("Arial", 20))
        self.bouton4.pack(padx=5, pady=5, side="left", fill="both", expand=True)

        self.frame3 = tk.Frame(self.frame)
        self.frame3.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame3, text="4", font=("Arial", 20))
        self.bouton1.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame3, text="5", font=("Arial", 20))
        self.bouton2.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton3 = tk.Button(self.frame3, text="6", font=("Arial", 20))
        self.bouton3.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton4 = tk.Button(self.frame3, text="+", font=("Arial", 20))
        self.bouton4.pack(padx=5, pady=5, side="left", fill="both", expand=True)

        self.frame4 = tk.Frame(self.frame)
        self.frame4.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame4, text="1", font=("Arial", 20))
        self.bouton1.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame4, text="2", font=("Arial", 20))
        self.bouton2.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton3 = tk.Button(self.frame4, text="3", font=("Arial", 20))
        self.bouton3.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton4 = tk.Button(self.frame4, text="=", font=("Arial", 20))
        self.bouton4.pack(padx=5, pady=5, side="left", fill="both", expand=True)

        self.frame5 = tk.Frame(self.frame)
        self.frame5.pack(fill="both", expand=True)
        self.bouton1 = tk.Button(self.frame5, text="0", font=("Arial", 20))
        self.bouton1.pack(padx=5, pady=5, side="left", fill="both", expand=True)
        self.bouton2 = tk.Button(self.frame5, text=".", font=("Arial", 20))
        self.bouton2.pack(padx=5, pady=5, side="left", fill="both", expand=True)





if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()