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

import pandas as pd
import matplotlib.pyplot as plt
import random

valeurs = 80 + 12 * np.random.standard_normal(size = 50)
satisfaction = ["Très Satisfait, Satisfait, Neutre, Insatisfait, Très Insatisfait"]
plt.xlim(10)
plt.ylim(25)

