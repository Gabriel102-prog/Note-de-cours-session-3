import tkinter as tk

class DemoRowspan(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("rowspan (exemple)")
        self.geometry("360x200")

        # container principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        content = tk.Frame(self, padx=10, pady=10)
        content.grid(row=0, column=0, sticky="nsew")

        # grille interne (2 colonnes × 2 lignes) qui peut s'étirer
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)

        # un bouton grand qui occupe 2 ligne (rowspan=2)
        tk.Button(content, text="=", font=("Segoe UI", 14, "bold")).grid(
            row=0, column=0, rowspan=2, sticky="nsew", padx=4, pady=4
        )

        # À droite : deux petits boutons empilés
        tk.Button(content, text="1").grid(row=0, column=1, sticky="nsew", padx=4, pady=4)
        tk.Button(content, text="2").grid(row=1, column=1, sticky="nsew", padx=4, pady=4)



if __name__ == "__main__":
    DemoRowspan().mainloop()
