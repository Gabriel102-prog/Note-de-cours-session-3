import tkinter as tk
# Importation de la classe Figure pour créer une figure Matplotlib
from matplotlib.figure import Figure
## Importation des outils nécessaires à l'intégration de Matplotlib dans Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("traçage d'une courbe")
        self.creer_graphe()

    def creer_graphe(self):

        # Création d'une figure Matplotlib
        fig = Figure(figsize=(5, 4))
        #le contenu de fig

        # Création du canvas Matplotlib (lié à la fenêtre Tkinter)
        canvas = FigureCanvasTkAgg(fig)
        canvas.draw()
        # Insertion du widget canvas dans la grille
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")


# Lancement de l'application
if __name__ == "__main__":
    app = App()
    app.mainloop()
