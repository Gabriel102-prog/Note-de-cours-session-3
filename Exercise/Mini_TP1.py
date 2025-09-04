# Exersice 1

# Exersice 2
import matplotlib.pyplot as plt
class CroissancePlante:
    def __init__(self, temps : list[float] , hauteur : list[float] ):
        self.__temps = []
        self.__hauteur = []
        self.imposer_croissance_temps()
    @property
    def temps(self):
        return self.__temps
    @property
    def hauteur(self):
        return self.__hauteur
    @temps.setter
    def temps(self, temps : list[float]):
        if not len(temps) == len(self.__hauteur):
            raise ValueError("Temps doit être égal à la hauteur")
        for i in temps:
            if i <= 0:
                raise ValueError("Le temps ne peut pas être négatif")
        self.__temps = temps
    @hauteur.setter
    def hauteur(self, hauteur : list[float]):
        if not len(hauteur) == len(self.__temps):
            raise ValueError("Temps doit être égal à la hauteur")
        for i in hauteur:
            if i <= 0:
                raise ValueError("Le temps ne peut pas être négatif")
        self.__temps = hauteur

    def ajouter_mesure(self, t: float, h: float):
        if not t <= 0 or not isinstance(t, int) or not isinstance(h, int):
            raise ValueError("Temps et hauteur doit être des entier et le temps doit être positif ")
        self.hauteur.append(h)
        self.temps.append(t) # TODO besoin de rapeler setter?
        self.imposer_croissance_temps()
        
    def imposer_croissance_temps(self):
        valeur = 0
        for i in self.temps:
            if i <= valeur:
                raise ValueError("Le temps n'est pas progressif")
            valeur = i


    def tracer(self):


plante = CroissancePlante
plante.ajouter_mesure(1, 3)
plante.tracer()