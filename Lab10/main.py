import random


# Zad1
class FibonacciOneClass:

    def __init__(self, max):
        self.first = 0
        self.second = 1
        self.iters = max
        self.current_iter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.first, self.second = self.second, self.first + self.second
        if self.current_iter < self.iters:
            self.current_iter += 1
            return self.first
        raise StopIteration


# iterator = FibonacciOneClass(10)

# for i in iterator:
#     print(i)
# for ite1 in iterator:
#     for ite2 in iterator:
#         print(f'{ite1} | {ite2}')


class FibonacciTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        return FibonacciTwoClass(self.max)


class FibonacciTwoClass:
    def __init__(self, ma):
        self.first = 0
        self.second = 1
        self.iters = ma
        self.current_iter = 0

    def __next__(self):
        self.first, self.second = self.second, self.first + self.second
        if self.current_iter < self.iters:
            self.current_iter += 1
            return self.first
        raise StopIteration


# iterator2 = FibonacciTwo(10)
#
# for ite1 in iterator2:
#     for ite2 in iterator2:
#         print(f'{ite1} | {ite2}')


# Zad3
m = 2 ** 48
c = 0


class RandomNumber01:

    def __init__(self):
        self.a = 44485709377909
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + c) % m
        return self.x


iter = RandomNumber01()
iterations = 0
circle_hits = 0
import math

while True:
    iterations += 1
    x = iter.__next__() / m * 2 - 1
    y = iter.__next__() / m * 2 - 1
    if x ** 2 + y ** 2 < 1:
        circle_hits += 1
    if math.fabs(math.pi - (circle_hits / iterations * 4)) < 1e-7:
        print(iterations)
        break
