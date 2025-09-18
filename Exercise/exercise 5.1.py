import tkinter as tk

# class Marius(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Gestionnaire de tâches")
#         self.geometry("900x1000")
#         self.create_widgets()
#
#     def create_widgets(self):
#         frame = tk.Frame(self)
#         frame.pack(side="top", fill="x")
#         tk.Label(frame, text="Ma To-Do List", font=("Arial",25), fg="black").pack(side="top", fill="x", pady=20)
#         tk.Entry(frame).pack(fill="y",pady=20, ipady =10, ipadx =40)
#
#         tk.Button(frame, text="Ajouter la tache").pack(fill="y",padx=350,pady=20)
#
#         tk.Listbox(frame, width=55, height=11).pack(padx=10, pady=20, ipady=10)
#
#         prioriteres = tk.BooleanVar(value=True)
#         tk.Checkbutton(frame,text="Toutes les taches sont prioritere",variable=prioriteres).pack(side="top", fill="x")
#
#         radio = tk.StringVar(value="Personnel")
#         rb1 = tk.Radiobutton(frame, text="Personnel", variable=radio, value="Personnel")
#         rb21 = tk.Radiobutton(frame, text="Professionel", variable=radio, value="Professionel")
#         rb1.pack(side="top", fill="x")
#         rb21.pack(side="top", fill="x")
#
#         label_notes = tk.Label(frame, text="Notes sur taches sélectionnée", font=("Arial",10), fg="black")
#         label_notes.pack(side="top", fill="x")
#
#         tk.Text(frame, width=50, height=10).pack( padx=100, pady=20,ipady=20)
#
#
# if __name__ == "__main__":
#     Marius().mainloop()



class Marius(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("800x100")
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self, borderwidth=2, relief="groove")
        frame.pack(fill="x",expand=True, padx=10, pady=10)

        frame_gauche = tk.Frame(frame)
        frame_gauche.pack(side="left")

        frame_droite = tk.Frame(frame)
        frame_droite.pack(side="right", fill="x")

        frame_centre = tk.Frame(frame, borderwidth=2)
        frame_centre.pack(side="left", fill="x")

        nom = tk.Label(frame_gauche, text="Nom:", font=("Arial", 10), fg="black")
        nom.pack(anchor="n")
        email = tk.Label(frame_gauche, text="Email:", font=("Arial", 10), fg="black")
        email.pack()

        entre1 = tk.Entry(frame_centre, width=100)
        entre1.pack(fill="x",pady=5)
        entre2 = tk.Entry(frame_centre, width=100)
        entre2.pack(fill="x",pady=5)

        tk.Button(frame_droite, text="Valider").pack(fill="x", pady=20, padx=20)




if __name__ == "__main__":
    Marius().mainloop()