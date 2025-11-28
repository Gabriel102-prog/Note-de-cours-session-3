import numpy as np

class Quadratique:
    def __init__(self, a, b, c):
        self.a = a
        if self.a == 0:
            raise ValueError("a ne peut pas etre égal a 0")
        self.b = b
        self.c = c

    def trouver_solution(self):
        x1 = (-self.b + np.sqrt((self.b ** 2) - 4 * self.a * self.c))/ 2 * self.a
        x2 = (-self.b - np.sqrt((self.b ** 2) - 4 * self.a * self.c)) / 2 * self.a
        resultat = (x1, x2)
        return resultat

essai = Quadratique(1, 3, -10)
print(essai.trouver_solution())


import matplotlib.pyplot as plt

valeurs = 80 + 12 * np.random.standard_normal(size = 25)
valeurs_sans_cent = []
for valeur in valeurs:
    if 100 <= valeur:
        valeur = 100
    valeurs_sans_cent.append(valeur)
print(valeurs)
print(valeurs_sans_cent)
plt.xlim(0, 100)
plt.ylim(0, 10)
plt.xlabel("Pourcentage de satisfaction")
plt.ylabel("Nombres de clients")
plt.title("Satisfaction clients")
plt.grid(True)

plt.hist(valeurs_sans_cent, width=4)
plt.show()

satisfaction = ["Très Insatisfait", "Très Inatisfait", "Neutre", "Satisfait", "Très Satifait"]
nb_personnes_satisfaction = [0, 0, 0, 0, 0]
for valeurs in valeurs_sans_cent:
    if 0 <= valeurs <=20:
        nb_personnes_satisfaction[0] += 1
    elif 20 < valeurs <= 40:
        nb_personnes_satisfaction[1] += 1
    elif 40 < valeurs <= 60:
        nb_personnes_satisfaction[2] += 1
    elif 60 < valeurs <= 80:
        nb_personnes_satisfaction[3] += 1
    elif 80 < valeurs <= 100:
        nb_personnes_satisfaction[4] += 1

plt.ylim(0, 25)
plt.xlabel("Pourcentage de satisfaction")
plt.ylabel("Nombres de clients")
plt.title("Satisfaction clients")
plt.bar(satisfaction, nb_personnes_satisfaction)
print(nb_personnes_satisfaction)
plt.show()
