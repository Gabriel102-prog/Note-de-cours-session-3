import json

class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def __str__(self):
        return f"{self.nom}, {self.age} ans, vit à {self.ville}"

# Classe pour gérer le fichier JSON
class LecteurJSON:
    def __init__(self, chemin_fichier):
        self.chemin_fichier = chemin_fichier

    def lire_personnes(self):
        personnes = [] # Liste pour stocker les objets Personne
        with open(self.chemin_fichier, "r", encoding="utf-8") as f: #UTF-8  permet de lire des caractères accentués ou non latins
            data = json.load(f)  # charge le fichier JSON en tant que liste de dictionnaires
            for item in data:
                ## Crée un objet Personne pour chaque entrée du fichier
                personne = Personne(item["nom"], item["age"], item["ville"])
                personnes.append(personne)
        return personnes

lecteur = LecteurJSON("personnes.json")
liste_personnes = lecteur.lire_personnes()

for personne in liste_personnes:
    print(personne)
