# classe métier de fusée gère les erreurs et les mauvaises entrées
from tkinter import messagebox


class Fusee:
    def __init__(self, nom, cap, vit):
        self.nom_fusee = nom
        self.capacite = cap
        self.vitesse_max = vit
        self.carburant = ""
        self.angle = ""

    @property
    def nom_fusee(self):
        return self.__nom_fusee

    @nom_fusee.setter
    def nom_fusee(self, nom):
        self.__nom_fusee = nom

    @property
    def capacite(self):
        return self.__capacite

    @capacite.setter
    def capacite(self, cap):
        try:
            e = float(cap)
            if e < 500000:
                self.__capacite = cap
            else:
                self.__capacite = ""
        except ValueError:
            self.__capacite = ""

    @property
    def vitesse_max(self):
        return self.__vitesse_max

    @vitesse_max.setter
    def vitesse_max(self, vit):
        try:
            e = float(vit)
            if e <= 8000:
                self.__vitesse_max = e
            else:
                self.__vitesse_max = ""
        except ValueError:
            self.__vitesse_max = ""

    @property
    def carburant(self):
        return self.__carburant

    @carburant.setter
    def carburant(self, carb):
        try:
            float(carb)
            if carb <= self.__capacite:
                self.__carburant = carb
            else:
                self.__carburant = ""
        except ValueError:
            self.__carburant = ""

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, ang):
        try:
            e = float(ang)
            if 1 <= e <= 90:  # pour meilleure vision de la courbe angle entre 1 et 90 == valide
                self.__angle = ang
            else:
                self.__angle = ""
        except ValueError:
            self.__angle = ""

    def verif_angle_carburant(self):
        if self.angle == "":
            messagebox.showerror("Error", "Angle doit être un float entre 1 et 90 degré")
            return False
        if self.carburant == "" or self.carburant > self.capacite:
            messagebox.showerror("Error", "Le carburant doit être un float et <= capacité de la fusée")
            return False
        return True


    def verification_init(self):
        if not self.nom_fusee:
            messagebox.showerror("Erreur nom fusée", "Nom de la fusée doit être non-vide.\nVeuillez réessayer")
            return False
        if not self.capacite:
            messagebox.showerror("Erreur capacité",
                                 "La capacité de la fusée doit être un réel <= 500000 L.\nVérifiez que l'entrée n'est pas vide, réessayez")
            return False
        if not self.vitesse_max:
            messagebox.showerror("Erreur vitesse limite", "La vitesse limite de la fusée doit être <= 8000.\nVérifiez que l'entrée n'est pas vide, réessayez")
            return False
        return True