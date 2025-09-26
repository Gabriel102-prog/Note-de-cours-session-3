# Exersice 1
import random
import matplotlib.pyplot as plt
class Montecarlo:
    def __init__(self,nb_points ):
        self.nb_points = nb_points
        self.x_int = []
        self.y_int = []
        self.x_ext = []
        self.y_ext = []
        self.point_dans_cercle = 0

    def generer_points(self):
        for i in range(self.nb_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

            if x**2 + y**2 <= 1:
                self.x_int.append(x)
                self.y_int.append(y)
                self.point_dans_cercle += 1
            else:
                self.x_ext.append(x)
                self.y_ext.append(y)

    def estimer_pi(self):
        return 4 * self.point_dans_cercle / self.nb_points

    def representation_points(self):
        plt.figure(figsize=(6, 6))
        plt.title("Montecarlo représentation")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.plot(self.x_int, self.y_int, 'og')
        plt.plot(self.x_ext, self.y_ext, 'or')
        plt.show()

objet = Montecarlo(10000)
objet.generer_points()
objet.representation_points()

# Exersice 2

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
        self.__hauteur = hauteur

    def ajouter_mesure(self, t: float, h: float):
        if t <= 0 or not isinstance(t, int) or not isinstance(h, int):
            raise ValueError("Temps et hauteur doit être des entier et le temps doit être positif ")
        self.hauteur.append(h)
        self.temps.append(t)
        self.imposer_croissance_temps()

    def imposer_croissance_temps(self):
        valeur = 0
        for i in self.temps:
            print(i,valeur)
            if i <= valeur:
                raise ValueError("Le temps n'est pas progressif")
            valeur = i


    def tracer(self):
        if len(self.__hauteur) == 0 or len(self.__temps) == 0:
            raise ValueError("Il y a aucune valeur de temps ou de hauteur")
        plt.title("Croissance de la plante")
        plt.ylabel("Hauteur (cm)")
        plt.xlabel("Temps (jours)")
        plt.xlim(0, (max(self.__temps) + 1))
        plt.ylim(0, (max(self.__hauteur) + 1))
        plt.plot(self.temps, self.hauteur, "sg--")
        plt.show()

plante = CroissancePlante()
plante.ajouter_mesure(1, 3)
plante.ajouter_mesure(2, 4)
plante.ajouter_mesure(8, 3)
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
        if not isinstance(annee, int):raise ValueError("Vous n'avez pas entrez un année positif")
        if annee <= 0: raise ValueError("L'année doit être positive")
        self.__annee = annee

    def emprunter(self) -> None :
        if not self.disponible:
            raise ValueError("Le document n'est pas disponible")
        self.__disponible = False

    def rendre(self) -> None :
        if self.disponible:
            raise ValueError("Le document est déja disponible")
        self.__disponible = True

    def __str__(self):
        dispo = "Oui" if self.__disponible else "Non"
        return (f"Le id du document est: {self.__id}, son titre est: {self.__titre}, son année est : {self.__annee} "
                f"et dispo: {dispo} ")


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
        self.__nom = nom.strip().title()
    @property
    def emprunts(self):
        return self.__emprunts.copy()
    # TODO pas sur comprend pk dans lecture

    def releve(self):
        return self.__journal.copy()

    def limite_emprunts(self):
        return 3

    def emprunter(self, document: Document) -> None:
        if not document.disponible:
            raise ValueError("Le document n'est pas disponible")

        if isinstance(document, Magazine):
            for i in self.__emprunts:
                if isinstance(i, Magazine):
                    raise ValueError("Vous avez déjà un magazine, impossible d'en emprunter un deuxième")

        if len(self.__emprunts) >= self.limite_emprunts():
            raise ValueError(f"Vous avez déjà atteint la limite de {self.limite_emprunts()} emprunts")
        document.emprunter()
        self.__emprunts.append(document)
        self.__journal.append(f"emprun:{document.titre}")

    def rendre(self, document: Document) -> None:
        if document.disponible:
            raise ValueError("Le document n'a jamais été emprunter")
        document.rendre()
        self.__emprunts.remove(document)
        self.__journal.append(f"retour:{document.titre}")
    def __str__(self):
        return f"L'id est: {self.__id}, le nom est: {self.__nom} et le nombre d'emprunt est de: {len(self.__emprunts)} "



class AdherentPremium(Adherent):
    def __init__(self, id: str, nom: str, emprunts: list[Document], journal: list[str]):
        super().__init__(id, nom, emprunts, journal)

    def limite_emprunts(self):
        return 5

class Bibliotheque:
    def __init__(self,documents: list[Document]):
        self.__documents = documents

    @property
    def documents(self):
        return self.__documents.copy()

    def ajouter_document(self, document: Document) -> None:
        if not isinstance(document, Document):
            raise TypeError("Le document doit être une instance de la classe Document")
        self.__documents.append(document)
    def rechercher_par_titre(self, mot: str) -> list[Document]:
        resultat_recherche = []
        for i in self.__documents:
            if mot in i.titre:
                resultat_recherche.append(i)
        return resultat_recherche

livre1 = Livre("L1", "Python Facile", 2022, "Dupont", 300)
livre2 = Livre("L2", "Programmation Orientée Objet", 2021, "Martin", 450)
mag1 = Magazine("M1", "Science & Vie", 2023, 45)
dvd1 = DVD("D1", "Inception", 2010, 148)

# Création d'une bibliothèque avec une liste de documents
biblio = Bibliotheque([livre1, livre2, mag1, dvd1])

print("Documents dans la bibliothèque :")
for doc in biblio.documents:
    print(" -", doc)

# Recherche d’un document par titre
print("\nRecherche 'Python' dans les titres :")
resultats = biblio.rechercher_par_titre("Python")
for doc in resultats:
    print("  ->", doc)

# Création d’adhérents
adh1 = Adherent("A1", "Alice", [], [])
adh2 = AdherentPremium("A2", "Bob", [], [])

# Emprunt par Alice
print("\nAlice emprunte 'Python Facile'...")
adh1.emprunter(livre1)
print(adh1)
print("Journal d'Alice :", adh1.releve())

# Tentative d'emprunt du même livre par Bob (doit lever une erreur car indisponible)
try:
    adh2.emprunter(livre1)
except ValueError as e:
    print("\nErreur attendue :", e)

# Bob emprunte un autre livre
print("\nBob emprunte 'Programmation Orientée Objet'...")
adh2.emprunter(livre2)
print(adh2)
print("Journal de Bob :", adh2.releve())

# Alice rend son livre
print("\nAlice rend son livre...")
adh1.rendre(livre1)
print(adh1)
print("Journal d'Alice :", adh1.releve())
