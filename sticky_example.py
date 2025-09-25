import tkinter as tk

class DemoSticky(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("sticky (exemple)")
        self.geometry("420x160")

        # container principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        content = tk.Frame(self, padx=8, pady=8)
        content.grid(row=0, column=0, sticky="nsew")

        # deux colonnes extensibles
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        content.columnconfigure(2, weight=1)
        content.columnconfigure(3, weight=1)
        content.rowconfigure(0, weight=1)

       
        tk.Label(content, text="Centré", bd=2, relief="groove").grid(
            row=0, column=0, padx=6, pady=6)
        tk.Label(content, text="Remplit (nsew)", bd=2, relief="groove").grid(
            row=0, column=1, sticky="nsew", padx=6, pady=6)

        tk.Label(content, text="nord-sud", bd=2, relief="groove").grid(
            row=0, column=2, sticky="nsew", padx=6, pady=6)

        tk.Label(content, text="est-ouest", bd=2, relief="groove").grid(
            row=0, column=3, sticky="ew", padx=6, pady=6)

if __name__ == "__main__":
    DemoSticky().mainloop()
