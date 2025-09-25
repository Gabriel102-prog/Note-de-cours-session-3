import tkinter as tk

class Demo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("columnspan exemple")
        self.geometry("420x160")

        # Conteneur principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.content = tk.Frame(self, padx=10, pady=10)
        self.content.grid(row=0, column=0, sticky="nsew")

        # colonnes internes : les colonnes 1 et 2 peuvent s'élargir
        self.content.columnconfigure(1, weight=1)
        self.content.columnconfigure(2, weight=1)

        # ligne 0 — sans columnspan (l'entrée ne prend qu'une seule colonne)
        tk.Label(self.content, text="Sans columnspan").grid(row=0, column=0, sticky="e", padx=4, pady=4)
        self.e1 = tk.Entry(self.content)
        self.e1.grid(row=0, column=1, sticky="ew", padx=4, pady=4)
        tk.Button(self.content, text="OK").grid(row=0, column=2, sticky="ew", padx=4, pady=4)

        # ligne 1 — avec columnspan=2 (l'entrée occupe les colonnes 1 et 2)
        tk.Label(self.content, text="Avec columnspan=2").grid(row=1, column=0, sticky="e", padx=4, pady=4)
        self.e2 = tk.Entry(self.content)
        self.e2.grid(row=1, column=1, columnspan=2, sticky="ew", padx=4, pady=4)

if __name__ == "__main__":
    Demo().mainloop()
