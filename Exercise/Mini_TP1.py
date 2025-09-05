# Exersice 1
class Montecarlo:
    def __init__(self, N):
        self.N = N


# Exersice 2
import matplotlib.pyplot as plt
class CroissancePlante:
    def __init__(self ):
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
        if not len(self.temps) == len(self.__hauteur):
            raise ValueError("Temps doit être égal à la hauteur")
        for i in temps:
            if i <= 0:
                raise ValueError("Le temps ne peut pas être négatif")
        self.__temps = temps
    @hauteur.setter
    def hauteur(self, hauteur : list[float]):
        if not len(self.hauteur) == len(self.__temps):
            raise ValueError("Temps doit être égal à la hauteur")
        for i in hauteur:
            if i <= 0:
                raise ValueError("Le temps ne peut pas être négatif")
        self.__temps = hauteur

    def ajouter_mesure(self, t: float, h: float):
        if t <= 0 or not isinstance(t, int) or not isinstance(h, int):
            raise ValueError("Temps et hauteur doit être des entier et le temps doit être positif ")
        self.hauteur.append(h)
        self.temps.append(t) # TODO besoin de rapeler setter?
        self.imposer_croissance_temps()
        
    def imposer_croissance_temps(self):
        valeur = 0
        for i in self.temps:
            print(i,valeur)
            if i <= valeur:
                raise ValueError("Le temps n'est pas progressif")
            valeur = i


    def tracer(self):
        if len(self.hauteur) == 0 or len(self.temps) == 0:
            raise ValueError("Il y a aucune valeur de temps ou de hauteur")
        plt.title("Croissance de la plante")
        plt.ylabel("Hauteur (cm)")
        plt.xlabel("Temps (jours)")
        plt.xlim(0, (max(self.__temps) + 1))
        plt.ylim(0, (max(self.__hauteur) + 1))
        plt.plot(self.temps, self.hauteur, "sg--")
        plt.show()
        # TODO Fournir des getters/propriétés pour lire temps et hauteurs sans exposer directement les listes privées
plante = CroissancePlante()
plante.ajouter_mesure(1, 3)
plante.ajouter_mesure(2, 4)
plante.ajouter_mesure(8, 3)
plante.ajouter_mesure(3,7)
plante.tracer()

# Exercise 3
class  Document:
    def __init__(self, id: str, titre: str, annee: int):
        self.__id = id
        self.__titre = titre
        self.__annee = annee
        self.__disponible = True
    @property
    def id(self):
        return self.__id
    @property
    def titre(self):
        return self.__titre
    @property
    def annee(self):
        return self.__annee
    @property
    def disponible(self):
        return self.__disponible

    @titre.setter
    def titre(self, titre):
        if not titre.strip():
            raise ValueError("Vous n'avez entrez aucun titre")
        self.__titre = titre
    @annee.setter
    def annee(self, annee):
        if not isinstance(annee, int):
            raise ValueError("Vous n'avez pas entrez un année positif")

    def emprunter(self) -> None :
        if not self.disponible:
            raise ValueError("Le document n'est pas disponible")
        self.__disponible = False

    def rendre(self) -> None :
        if self.disponible:
            raise ValueError("Le document est déja disponible")
        self.__disponible = True

    def __str__(self):
        return (f"Le id du document est: {self.__id}, son titre est: {self.__titre}, son année est : {self.__annee} "
                f"et il est {self.__disponible} que se document est diponible")  #TODO regarder si représentation correcte


class Livre(Document):
    def __init__(self, id: str, titre: str, annee: int, auteur: str, nb_pages: int):
        super().__init__(id, titre, annee)
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self, auteur):
        if not auteur.strip():
            raise ValueError("Vous n'avez entrez aucune auteur")
        self.__auteur = auteur
    @property
    def nb_pages(self):
        return self.__nb_pages
    @nb_pages.setter
    def nb_pages(self, nb_pages):
        if not 1 <= nb_pages:
            raise ValueError("Vous n'avez pas entrez un nb pages positif")
        self.__nb_pages = nb_pages

class Magazine(Document):
    def __init__(self, id: str, titre: str, annee: int, numero: int):
        super().__init__(id, titre, annee)
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        if not 1 <= numero:
            raise ValueError("Vous n'avez pas entrez un numero positif")
        self.__numero = numero


class DVD(Document):
    def __init__(self, id: str, titre: str, annee: int, duree_min: int):
        super().__init__(id, titre, annee)
        self.__duree_min = duree_min
        if duree_min < 0:
            raise ValueError("la duré doit être supérieur a 0")


class Adherent:
    def __init__(self, id: str, nom: str, emprunts: list[Document], journal: list[str]):
        self.__id = id
        self.__nom = nom
        self.__emprunts = emprunts
        self.__journal = journal

    @property
    def id(self):
        return self.__id
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        if not nom.strip():
            raise ValueError("Vous n'avez pas entrez de nom")
        self.__nom = nom  #TODO  nom (lecture/écriture : non vide, title())
    @property
    def emprunts(self):
        return self.__emprunts.copy()
    # TODO pas sur comprend pk dans lecture

    def releve(self):
        return self.__journal.copy()

    def limite_emprunts(self):
        return 3  #TODO je ne comprend pas sa sert a quoi

    def emprunter(self, doc: Document) -> None:
        pass
    def rendre(self, doc: Document) -> None:
        pass
    def __str__(self):
        return f"L'id est: {self.__id}, le nom est: {self.__nom} et le nombre d'emprunt est de: {len(self.__emprunts)} "
        # TODO ?



