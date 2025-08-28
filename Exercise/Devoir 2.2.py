class Etudiant:
    def __init__(self, id:int, nom:str):
        self.__id = id
        self.__nom = nom
        self.__notes = {}

    @property
    def id(self):
        return self.__id
    @property
    def nom(self):
        return self.__nom
    @property
    def notes(self):
        return self.__notes
    @id.setter
    def id(self, id:str):
        if not isinstance(id,int):
            raise ValueError("ID non valide")
        else:
            self.__id = id
    @notes.setter
    def notes(self, notes):
        if not isinstance(notes.keys(),str) or not 0 < notes.values() < 20:
            raise ValueError("Note ou nom de la matière non valide!!")


    def ajouter_note(self, matiere: str, note: float):
        self.__notes[matiere] = note
    def moyenne(self):
        for matiere in self.__notes.:

    def __str__(self):
        pass
class Groupe:
    def __init__(self,etudiants:list):
        super().__init__()

        self.etudiants = etudiants

    def afficher_etudiants(self):
        pass
