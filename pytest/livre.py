

STATUTS = ("disponible", "indisponible", "précommande")

class Livre:

    def __init__(self, statut, isbn, titre, auteur):
        self.statut = statut
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.__quantite_stock = 0

    # --- statut ---
    @property
    def statut(self):
        return self.__statut

    @statut.setter
    def statut(self, valeur):
        if valeur in STATUTS:
            self.__statut = valeur
        else:
            raise ValueError(f"Le statut doit appartenir à {STATUTS}.")

    # --- isbn ---
    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, valeur):
        if isinstance(valeur, str) and valeur.strip():
            self.__isbn = valeur.strip()
        else:
            raise ValueError("L'ISBN doit être une chaîne non vide.")

    # --- titre ---
    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, valeur):
        if isinstance(valeur, str) and valeur.strip():
            self.__titre = valeur.strip()
        else:
            raise ValueError("Le titre doit être une chaîne non vide.")

    # --- auteur ---
    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, valeur):
        if isinstance(valeur, str) and valeur.strip():
            self.__auteur = valeur.strip()
        else:
            raise ValueError("Le nom de l’auteur doit être une chaîne non vide.")

    # --- quantite_stock ---
    @property
    def quantite_stock(self):
        return self.__quantite_stock

    # --- opérations métier ---
    def achat(self, qte):
        """Ajoute une quantité au stock."""
        q = int(qte)
        if q <= 0:
            raise ValueError("La quantité achetée doit être > 0.")
        self.__quantite_stock += q

    def vente(self, qte):
        """Retire une quantité du stock si disponible."""
        q = int(qte)
        if q <= 0:
            raise ValueError("La quantité vendue doit être > 0.")
        if q > self.__quantite_stock:
            raise ValueError("Stock insuffisant pour la vente.")
        self.__quantite_stock -= q

    # --- nouvelles fonctions ---
    def changer_statut(self, nouveau_statut):
        """Modifie le statut du livre si valide."""
        if nouveau_statut not in STATUTS:
            raise ValueError(f"Statut invalide. Valeurs possibles : {STATUTS}")
        self.__statut = nouveau_statut

    def infos(self):
        """Retourne les infos du livre sous forme de dictionnaire."""
        return {
            "titre": self.titre,
            "auteur": self.auteur,
            "isbn": self.isbn,
            "statut": self.statut,
            "stock": self.quantite_stock
        }

    def __str__(self):
        return (f"{self.titre} par {self.auteur} "
                f"(ISBN: {self.isbn}, Statut: {self.statut}) - "
                f"Stock: {self.quantite_stock}")
