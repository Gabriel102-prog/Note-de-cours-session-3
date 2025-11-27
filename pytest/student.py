# student.py
class Student:

    def __init__(self, name: str):
        self.name = name
        self._grades = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le nom doit etre non vide.")
        self._name = value.strip()

    @property
    def grades(self):
        return list(self._grades)

    def add_note(self, note: int):
        if not isinstance(note, int):
            raise TypeError("La note doit être un entier.")
        if not 0 <= note <= 100:
            raise ValueError("La note doit être comprise entre 0 et 100.")
        self._grades.append(note)

    def average(self) :
        if not self._grades:
            raise ValueError("Aucune note pour calculer la moyenne.")
        return sum(self._grades) / len(self._grades)

    def best(self):
        if not self._grades:
            raise ValueError("Aucune note.")
        return max(self._grades)

    def status(self) :
        if not self._grades:
            return "echec"
        if self.average() >= 60 and min(self._grades) >= 40:
            return "admis"
        else:
            return "echec"
