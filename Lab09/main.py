from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


class IFS:

    def __init__(self, wspolczynniki_przeksztalcenia, prawdobodobienstwo=None):
        self.wspolczynniki = wspolczynniki_przeksztalcenia
        if prawdobodobienstwo is not None:
            self.probability = [1 / len(wspolczynniki_przeksztalcenia) for i in
                                range(len(wspolczynniki_przeksztalcenia))]
        else:
            self.probability = prawdobodobienstwo
        self.x = [0, ]
        self.y = [0, ]

    def przeksztalcenia(self, iterations):
        for i in range(iterations):
            p = self.wspolczynniki[np.random.choice(len(self.wspolczynniki), 1, p=self.probability)[0]]
            self.x.append(p[0] * self.x[i] + p[1] * self.y[i] + p[2])
            self.y.append(p[3] * self.x[i] + p[4] * self.y[i] + p[5])

    def draw(self):
        plt.plot(self.x, self.y, 'b, ')
        plt.savefig('zad1')
        plt.clf()


# Zad2


# ifs = IFS(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065),
#            (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236),
#            (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)),
#           (0.90, 0.05, 0.05))
ifs = IFS(((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513),
           (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536),
           (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235),
           (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569),
           (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113),
           (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536),
           (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487),
           (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716),
           (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714),
           (-0.121, 0, 5.941, 0, 0.053, 1.487)))
ifs.przeksztalcenia(10 ** 6)
ifs.draw()


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __iadd__(self, vector):
        return self + vector

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value, self.z * value)

    def __len__(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __str__(self):
        return f"[x:{self.x} y:{self.y} z:{self.z}]"

    def dot_product(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def vector_product(self, vector):
        return Vector(self.y * vector.z - self.z * vector.y,
                      self.z * vector.x - self.x * vector.z,
                      self.x * vector.y - self.y * vector.x)

    def mixed_product(self, v, w):
        return Vector(self.y * v.z - self.z * v.y,
                      self.z * v.x - self.x * v.z,
                      self.x * v.y - self.y * v.x).dot_product(w)


# print(Vector(1, 0, -2).vector_product(Vector(-1, 1, 1)))
# print(Vector(1, -2, -1).mixed_product(Vector(3, 2, 1), Vector(1, -1, 0)))


# Zad3
class StaticMethod:

    @staticmethod
    def strumien_indukcji(B, S):
        return B.dot_product(S)

    @staticmethod
    def lorentz_force(q, E, v, B):
        return (E + v.vector_product(B)) * q

    @staticmethod
    def work_lorentz_force(q, E, v):
        return E.dot_product(v) * q


print(StaticMethod.strumien_indukcji(Vector(1, 1, 2), Vector(2, 2, 2)))
print(StaticMethod.lorentz_force(1, Vector(1, 1, 2), Vector(2, 2, 2), Vector(1, 2, 3)))
print(StaticMethod.work_lorentz_force(1, Vector(1, 1, 2), Vector(1, 2, 3)))
