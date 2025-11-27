from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np


class Tracercourbe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traceur de courbes")
        self.geometry("600x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.frame1 = tk.Frame(self)
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=1)
        self.frame1.columnconfigure(0, weight=1)
        self.label = ttk.Label(self.frame1, text="TraceurChoisir le type de courbe")
        self.label.grid(row=0, column=0, sticky="ew",padx=50,pady=5)
        self.bt = ttk.Button(self.frame1,text="Ajouter", command=self.ajouter)
        self.bt.grid(row=0, column=1,rowspan=2, sticky="we",padx=100)
        self.variable = tk.StringVar()
        self.menu_deroulant = ttk.Combobox(self.frame1, textvariable=self.variable)
        self.menu_deroulant['values'] = ("Courbe linéaire (sinus)", "Nuage de points (scatter)", "Diagramme en barres")
        self.menu_deroulant.current(0)
        self.menu_deroulant.grid(row=1, column=0, sticky="w",padx=50)
        self.frame2 = tk.Frame(self)
        self.frame2.grid(row=1, column=0, sticky="nsew")


        self.fig= Figure(figsize= (5,5))
        self.gab = self.fig.add_subplot()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.widget= self.canvas.get_tk_widget()
        self.widget.grid(row=2, column=0, sticky="ew")

    def ajouter(self):
        self.gab.clear()

        type_graphique = self.variable.get()

        if type_graphique == "Courbe linéaire (sinus)":
            x = np.linspace(0, 10, 100)
            y = np.sin(x)
            self.gab.plot(x, y, label="sin(x)", color="red")
            self.gab.set_title("Courbe linéaire")

        elif type_graphique == "Nuage de points (scatter)":
            x = np.linspace(0, 10, 100)
            y = np.sin(x)
            self.gab.scatter(x, y, label="sin(x)", color="blue")
            self.gab.set_title("Nuage de points")

        elif type_graphique == "Diagramme en barres":
            noms = ["Gabriel", "Mathias", "Maé"]
            ages = [19, 21, 14]
            self.gab.bar(noms, ages, color="green")
            self.gab.set_title("Diagramme en barres")

        self.gab.set_xlabel("x")
        self.gab.set_ylabel("y")
        self.canvas.draw()




if __name__ == "__main__":
    Tracercourbe().mainloop()