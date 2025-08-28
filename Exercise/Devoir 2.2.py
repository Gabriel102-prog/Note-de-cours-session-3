class Etudiant:
    def __init__(self, identite:int, nom:str):
        self.__id = identite
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
    def id(self, identite:str):
        if not isinstance(identite,int):
            raise ValueError("ID non valide")
        else:
            self.__id = id
    @notes.setter
    def notes(self, note: tuple):
        if not isinstance(note[0], str) or not 0 <= note[1] <= 20:
            raise ValueError("Note ou nom de la matière non valide!!")
        self.__notes[note[0]] = note[1]

    def ajouter_note(self, matiere: str, note: float):
        self.notes = (matiere, note)

    def moyenne(self):
        total = 0
        nb_notes = 0
        if not len(self.__notes) == 0:
            for matiere in self.__notes.values():
                total += matiere
                nb_notes += 1
            return total / nb_notes
        return 0

    def __str__(self):
        return f"{self.__nom} à comme identifiant {self.__id} et a une moyenne de {round(self.moyenne(), 2)}"



class Groupe:
    def __init__(self, etudiants=None):  # TODO
        if etudiants:
            self.etudiants: list[Etudiant] = []
        else:
            self.etudiants = list(etudiants)


    def ajouter_etudiant(self, etudiant: Etudiant):
        self.etudiants.append(etudiant)

    def afficher_etudiants(self):
        nb_etudiants =0
        for i in self.etudiants:
            nb_etudiants += 1
            print(f"Étudiant{nb_etudiants}: id:{i.id}, nom:{i.nom}, moyenne:{round(i.moyenne(), 2)}")

    def meilleur_etudiant(self):
        if not self.etudiants:
            return None
        meilleur = max(self.etudiants, key=lambda e: e.moyenne())
        return meilleur.nom

    def notes_par_matiere(self):
        matieres ={}
        for i in self.etudiants:
            for matiere, note in i.notes.items():
                if matiere not in matieres:
                    matieres[matiere] = []
                matieres[matiere].append(note)
        return matieres



etudiant_1 = Etudiant(1234,"Samuel")
etudiant_1.ajouter_note("Math", 7)
etudiant_1.ajouter_note("Francais", 17)
etudiant_1.ajouter_note("Physique", 16)

etudiant_2 = Etudiant(1235, "Marius")
etudiant_2.ajouter_note("Math", 13)
etudiant_2.ajouter_note("Francais", 17)
etudiant_2.ajouter_note("Physique", 8)

etudiant_3 = Etudiant(1236, "Édouard")
etudiant_3.ajouter_note("Math", 18)
etudiant_3.ajouter_note("Francais", 10)
etudiant_3.ajouter_note("Physique", 16)

groupe = Groupe((etudiant_1,etudiant_2, etudiant_3))
groupe.afficher_etudiants()
print(groupe.meilleur_etudiant())
print(groupe.notes_par_matiere())