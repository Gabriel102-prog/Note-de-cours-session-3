
class CompteBancaire:
    def __init__(self, titulaire, numero_compte,solde):
        self.__titulaire = titulaire
        self.__numero_compte = numero_compte
        if solde == 0 or solde < 0:
            self.__solde = 0
        else:
            self.__solde = solde
        self.__historique = []
    @property
    def titulaire(self):
        return self.__titulaire
    @property
    def numero_compte(self):
        return self.__numero_compte
    @property
    def historique(self):
        historique_copie = self.__historique
        return historique_copie
    @property
    def solde(self):
        return self.__solde

    @numero_compte.setter
    def numero_compte(self):
        if self.__numero_compte >= 0 :
            return True
        else: return False
    # TODO Chaque modification est enregistrée dans l'historique

    def deposer(self,montant):
        if 0 > montant:
            return "Le montant déposer est invalide"
            raise ValueError

        else:
            self.__solde += montant
            self.__historique.append(f"Dépot:+{montant}, Solde:{self.__solde}")
    def retirer(self,montant):
        if montant < 0:
            return "Le montant a retirer est invalide"
        if montant > self.__solde:
            return "Vous n'avez pas assez de fond"
        else:
            self.__solde -= montant
            self.__historique.append(f"Retrait:-{montant}, Solde:{self.__solde}")

    def __str__(self):
        return f"Le propriétaire du Compte numéro {self.__numero_compte} est {self.__titulaire}. Le solde actuel est {self.__solde}$"


compte = CompteBancaire("Samuelle", "1234", 525)
compte.deposer(20)
compte.retirer(20)
print (f"Le solde est de {compte.solde}")
print (f"L'historique est {compte.historique}")


