# Zad1
from math import sqrt
import time
from sys import version
import random

powt = 1000
N = 10000


def tester(func):
    ti = time.time_ns()
    for r in range(powt):
        func()
    return time.time_ns() - ti


def forStatement():
    lista = []
    for n in range(N):
        lista.append(n)
    return lista


def listComprehension():
    return [x for x in range(N)]


def mapFunction():
    return map(lambda x: x, range(N))


def generatorExpression():
    return (x for x in range(N))


print(version)
test = (forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

# Zad2


list1 = [random.randrange(0, 20) for i in range(100)]
list2 = [random.randrange(0, 20) for x in range(100)]

print(list(filter(lambda x: (x[0] + x[1] > 2) and (x[0] + x[1] < 15), zip(list1, list2))))


# Zad3
def zad3(list_x, list_y):
    n = len(list_x)
    x_daszkiem = sum(list_x) / n
    y_daszkiem = sum(list_x) / n
    D = sum([(x - x_daszkiem) ** 2 for x in list_x])
    list_of_points = zip(list_x, list_y)
    a = sum(map(lambda x: x[1] * (x[0] - x_daszkiem), list_of_points)) / D
    b = y_daszkiem - a * x_daszkiem
    delta_y = sqrt(sum(map(lambda x: pow(x[1] - a * x[0] + b, 2), list_of_points)) / (n - 2))
    delta_a = delta_y / sqrt(D)
    delta_b = delta_y * sqrt((1 / n) + pow(x_daszkiem, 2) / D)
    return a, delta_a, b, delta_b, D


print(zad3([1, 2, 3], [1, 2, 3]))


# Zad4

def myreduce(func, iter):
    result = iter[0]
    for i in range(1, len(iter)):
        result = func(result, iter[i])
    return result


print(myreduce(lambda x, y: x + y, [2, 2, 3]))
print(myreduce(lambda x, y: x * y, [2, 2, 3]))

# Zad5

lista_x_y = [[1, 1], [2, 2], [3, 3], [4, 4]]

print(myreduce(
    lambda lista, list_points: list(map(lambda x, y: x + [y] if isinstance(x, list) else [x, y], lista, list_points)),
    lista_x_y))
