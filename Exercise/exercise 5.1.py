import tkinter as tk

class Marius(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de tâches")
        self.geometry("900x1000")
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self)
        tk.pack()
        tk.Label(frame text="Ma To-Do List", front=("Arial",20), fg="black").pack(fill="x")

        list = tk.Frame(self, bg="gray", borderwidth=2, relief="ridge")
        list.pack(fill="x", padx=50, pady=5)




if __name__ == "__main__":
    Marius().mainloop()