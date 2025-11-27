import csv

# Classe représentant une personne
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def __str__(self):
        return f"{self.nom}, {self.age} ans, vit à {self.ville}"

    def en_liste(self):
        # Retourne les données sous forme de liste pour le CSV
        return [self.nom, self.age, self.ville]


# Classe pour écrire dans un fichier CSV
class EcritureCSV:
    def __init__(self, chemin_fichier):
        self.chemin_fichier = chemin_fichier

    def ecrire_personnes(self, liste_personnes):
        with open(self.chemin_fichier, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=",")
            # Écrire l'en-tête
            writer.writerow(["nom", "âge", "ville"])
            # Écrire chaque personne
            for personne in liste_personnes:
                writer.writerow([personne.nom, personne.age, personne.ville])


# === Utilisation ===

personnes = [
    Personne("Alice", 30, "Paris"),
    Personne("Bob", 25, "Lyon"),
    Personne("Charlie", 39, "Montréal")
]

ecrivain = EcritureCSV("personnes.csv")
ecrivain.ecrire_personnes(personnes)
