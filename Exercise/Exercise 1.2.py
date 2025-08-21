class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    @property
    def nom(self):
        return self.__nom

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError("Age must be greater than zero")
        self.__age = age

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    def __str__(self):
        return f"Le nom est {self.__nom} et l'age est {self.__age}"

p = Personne("Alice", 30)
print(p)


