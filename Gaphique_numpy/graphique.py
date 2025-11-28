import random


class Cercle:
    def __init__(self, nb_points):
        self.nb_points = nb_points
        self.nb_cercle = 0
        self.nb_carre = 0
    liste_x = [random.uniform(-1, 1)]
    liste_y = [random.uniform(-1, 1)]

    def dans_cercle(self):
        for i in range(0, self.nb_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            print(x ** 2 + y ** 2)
            if (x ** 2 + y ** 2) < 1:
                self.nb_cercle += 1
            else:
                self.nb_carre += 1

    def resultat(self):
        print(self.nb_cercle ,self.nb_carre)

cercle = Cercle(5)
cercle.resultat()

class MonteCarlo:
    def __init__(self, nombre_points = 10000):
        self.x_in = []
        self.y_in = []
        self.x_out = []
        self.y_out = []
        self.nombre_points = nombre_points
    def generer_point(self):
        for i in range(self.nombre_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x ** 2 + y ** 2 < 1:
                self.x_in.append(x)
                self.y_in.append(y)
            else:
                self.x_out.append(x)
                self.y_out.append(y)
    def estimer_pi(self):
        if self.nombre_points == 0:
            return 0
        else:
            return 4* len(self.x_in)/self.nombre_points
point = MonteCarlo()
point.generer_point()
print(point.estimer_pi())

