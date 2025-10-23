import json

# Classe représentant une personne
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def __str__(self):
        return f"{self.nom}, {self.age} ans, vit à {self.ville}"

    def en_dict(self):
        return {
            "nom": self.nom,
            "age": self.age,
            "ville": self.ville
        }
class EcritureJSON:
    def __init__(self, chemin_fichier):
        self.chemin_fichier = chemin_fichier

    def ecrire_personnes(self, liste_personnes):
        # On transforme chaque objet Personne en dictionnaire
        donnees = []
        for personne in liste_personnes:
            donnees.append(personne.en_dict())
        ## Écrit la liste de dictionnaires dans le fichier JSON avec une indentation
        with open(self.chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=4, ensure_ascii=False)

# Liste d'objets Personne
personnes = [
    Personne("Alice", 30, "Paris"),
    Personne("Bob", 25, "Lyon"),
    Personne("Charlie", 39, "Montréal")
]

# Écriture dans le fichier JSON
ecrivain = EcritureJSON("personnes.json")
ecrivain.ecrire_personnes(personnes)
