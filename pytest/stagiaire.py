class Stagiaire:
    def __init__(self, nom, age, num_inscription):
        self.__nom = nom
        self.__age = age
        self.__num_inscription = num_inscription

    def __lt__(self, other):
        """Compare si un stagiaire est plus jeune qu'un autre."""
        if not isinstance(other, Stagiaire):
            raise TypeError("L'opérande doit être un Stagiaire")
        return self.__age < other.__age

    def __str__(self):
        return f"Stagiaire: {self.__nom}, Âge: {self.__age}, Numéro: {self.__num_inscription}"