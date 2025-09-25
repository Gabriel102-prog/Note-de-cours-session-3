import tkinter as tk

class DemoColumnConfigure(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("columnconfigure (exemple)")
        self.geometry("420x160")

        # Conteneur principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        content = tk.Frame(self, padx=10, pady=10)
        content.grid(row=0, column=0, sticky="nsew")

        # réglage des colonnes du Frame: col 0 = 1 part, col 1 = 3 parts
        content.columnconfigure(0, weight=1)   # s'étire un peu
        content.columnconfigure(1, weight=3)   # s'étire 3x plus
        content.rowconfigure(0, weight=1)

        # Widgets (dans le Frame)
        tk.Button(content, text="Gauche").grid(row=0, column=0, sticky="nsew", padx=6, pady=6)
        tk.Button(content, text="Droite (3x)").grid(row=0, column=1, sticky="nsew", padx=6, pady=6)

        
if __name__ == "__main__":
    DemoColumnConfigure().mainloop()
