class Compte:
    def __init__(self, numero_compte:str,titulaire_compte: str, solde_compte: float, nbre_operations:int = 0):
        self.__numero_compte = numero_compte
        self.__titulaire_compte = titulaire_compte
        self.__solde_compte = solde_compte
        self.__nbre_operations = nbre_operations

    @property
    def numero_compte(self):
        return self.__numero_compte
    @property
    def titulaire_compte(self):
        return self.__titulaire_compte
    @property
    def solde_compte(self):
        return self.__solde_compte
    @property
    def nbre_operations(self):
        return self.__nbre_operations
    # TODO revoir partie propriété

    @solde_compte.setter
    def solde_compte(self, montant):
        if not isinstance(montant, (int, float)):
            raise ValueError("Montant non valide")
        if montant < 0:
            raise ValueError("Montant négatif")
        self.__solde_compte = montant
    @nbre_operations.setter
    def nbre_operations(self, nb_operations):
        if nb_operations < 0:
            raise ValueError("Nombre d'opération négative")
        self.__nbre_operations = nb_operations


    def deposer(self, montant: float):
        if montant <= 0:
            raise ValueError("Montant invalide (négatif)")
        self.__solde_compte += montant
        self.__nbre_operations += 1
        return True

    def retirer(self, montant: float):
        if montant <= 0:
            raise ValueError("Montant invalide (négatif)")
        if montant > self.__solde_compte:
            raise ValueError("Vous n'avez pas assez de fond")
        self.__solde_compte -= montant
        self.__nbre_operations += 1
        return True

    def __repr__(self):
        return f"Numéro:{self.__numero_compte}, Titulaire:{self.__titulaire_compte}, Solde: {self.__solde_compte}, Nombre opération: {self.__nbre_operations} "


class CompteCourant(Compte):
    def __init__(self, numero_compte,titulaire_compte, solde_compte, nbre_operations, frais_retrait):
        super().__init__( numero_compte,titulaire_compte, solde_compte, nbre_operations)
        self.__frais_retrait = frais_retrait
    @property
    def frais_retrait(self):
        return self.__frais_retrait
    @frais_retrait.setter
    def frais_retrait(self, frais):
        if frais <= 0:
            raise ValueError("Les frais de retrais doivent être positif")
        self.__frais_retrait = frais
    #TODO Redéfinit retirer(montant) : vérifie et débite montant + frais_retrait(refus si dépasse le solde).

    def retirer(self, montant: float): #TODO quesce que sa veut dire de débite le montant
        if montant <= 0:
            raise ValueError("Refus!!\nMontant invalide (négatif)")
        if montant + self.__frais_retrait > self.solde_compte:
            raise ValueError("Refus!!\nVous n'avez pas assez de fond")
        self.solde_compte -= (montant + self.__frais_retrait)
        self.nbre_operations += 1
        return True




class CompteEpargne(Compte):
    def __init__(self, numero_compte, titulaire_compte, solde_compte, nbre_operations, taux:float):
        super().__init__(numero_compte, titulaire_compte, solde_compte, nbre_operations)
        self.__taux = taux

    @property
    def taux(self):
        return self.__taux

    @taux.setter
    def taux(self, taux:float):
        if not 1 >= taux >= 0:
            raise ValueError("Le taux doit être comprit entre 0 et 1 inclusif")
        self.__taux = taux

    def capitaliser(self):
        if 0 >= self.solde_compte:
            raise ValueError("Votre solde est nul")
        self.solde_compte += (self.__taux * self.solde_compte)
        return True


class CompteRemunere(CompteEpargne):
    def __init__(self, numero_compte, titulaire_compte, solde_compte, nbre_operations, taux, palier: float,  bonus: float):
        super().__init__(numero_compte, titulaire_compte, solde_compte, nbre_operations, taux)
        self.__palier = palier
        self.__bonus = bonus

    @property
    def palier(self):
        return self.__palier

    @property
    def bonus(self):
        return self.__bonus

    @palier.setter
    def palier(self, palier):
        if 0 > palier:
            raise ValueError("Le palier est négatif")
        self.__palier = palier

    @bonus.setter
    def bonus(self, bonus):
        if not 1 >= bonus >= 0:
            raise ValueError("Le bonus doit être entre 0 et 1 inclusivement")
        self.__bonus = bonus

    def capitaliser(self):
        if 0 >= self.solde_compte:
            raise ValueError("Votre solde est nul")
        if self.solde_compte >= self.__palier:
            self.solde_compte += self.solde_compte * ((1 + self.__bonus) * (1 + self.taux) - 1)
            return True
        else:
            self.solde_compte += self.solde_compte * self.taux
            return False

class CompteCourantPlafonne(CompteCourant):
    def __init__(self,numero_compte,titulaire_compte, solde_compte, nbre_operations, frais_retrait,plafond: float, reste: float):
        super().__init__(numero_compte,titulaire_compte, solde_compte, nbre_operations, frais_retrait)
        self.__plafond = plafond
        self.__reste = reste
        self.__hist = []

 # TODO ou doit je mettre les condition si je veux seulement une lecture et non écriture

    @property
    def plafond(self):
        return self.__plafond
    @property
    def reste(self):
        return self.__reste
    @property
    def hist(self):
        return self.__hist

    @plafond.setter
    def plafond(self, plafond):
        if plafond < 0:
            raise ValueError("Le plafond doit être positif.")
        self.__plafond = plafond
        self.__reste = plafond
    @hist.setter
    def hist(self, hist):
        if not isinstance(hist,str):
            raise ValueError("Doit être mots")
        self.__hist = hist

    def reset_plafond(self):  # TODO je ne comprend pas sa sert a quoi
        self.__plafond = self.__reste

    def deposer(self, montant):
        succes = super().deposer(montant)
        if succes:
            self.__hist.append("DEPOT_OK")

    def retirer(self, montant):
        if self.__reste <= montant:
            self.__hist.append("REFUS_PLAFOND")
            return False
        if super().retirer(montant): # TODO pas bon mais sais pas pourquoi
            self.solde_compte -= montant
            montant -= self.__reste
            self.__hist.append("RETRAIT_OK")
            return True
        self.__hist.append("REFUS_SOLDE")
        return False

compte = CompteCourant("12345", "Gabriel Bertrand", 0, 0, 1.0)
compte.deposer(100)
compte.retirer(20)
print(compte.solde_compte) # Me donne 79.
#compte.retirer(100)

compte2 = CompteEpargne("1234", "Gabriel Bertrand", 0, 0, 0.05)
compte2.deposer(200)
compte2.capitaliser()
print(compte2.solde_compte) # Me donne 210.

compte3 = CompteRemunere("1234", "Gabriel Bertrand", 0, 0, 0.05, 1000, 0.10)
compte3.deposer(1000)
compte3.capitaliser()
print(compte3.solde_compte) # Me donne 1155.

compte4 = CompteCourantPlafonne("1234", "Gabriel Bertrand", 0, 0, 2, 300, 0)
compte4.deposer(500)
compte4.retirer(200)
compte4.retirer(150)
compte4.reset_plafond()
compte4.retirer(150)
print(compte4.hist)

