import csv

class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def __str__(self):
        return f"{self.nom}, {self.age} ans, vit à {self.ville}"

# Classe pour gérer le fichier CSV
class LecteurCSV:
    # Ici, le paramètre doit être un nom de variable, pas un nom de fichier avec extension
    def __init__(self, chemin_fichier):
        self.chemin_fichier = chemin_fichier

    def lire_personnes(self):
        personnes = [] #C’est une liste vide créée pour stocker tous les objets Personne que l’on va lire dans le fichier CSV.
        with open(self.chemin_fichier, "r", newline="", encoding="utf-8") as f:
            # newline =""permet de gérer correctement les fins de ligne dans les fichiers CSV
            lecteur = csv.reader(f, delimiter=";") #crée un objet qui va lire le fichier CSV ligne par ligne
            next(lecteur)  # Sauter l'en-tête
            for ligne in lecteur:
                nom, age, ville = ligne #cette ligne fait une décomposition.
                personne = Personne(nom, int(age), ville)
                personnes.append(personne)
        return personnes

lecteur = LecteurCSV("personnes.csv")
liste_personnes = lecteur.lire_personnes()

for personne in liste_personnes:
    print(personne)
