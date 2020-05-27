import math


# Zad1


class Point:
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    def __init__(self):
        self.x = 0
        self.y = 0


# punkt = Point()
# punkt.x = 12
# print(punkt.x)


# Zad2

def dek(punkt1, punkt2):
    def dek2(fun):
        def inner(p1, p2):
            if punkt1 <= p1.x <= punkt2 and punkt1 <= p1.y <= punkt2 and punkt1 <= p2.x <= punkt2 and punkt1 <= p2.y <= punkt2:
                return fun(p1, p2)
            else:
                raise ArithmeticError

        return inner

    return dek2


@dek(-5, 5)
def add(p1, p2):
    p = Point()
    p.x = p1.x + p2.x
    p.y = p1.y + p2.y
    return p


p1 = Point()
p2 = Point()
p1.x = 12
p1.y = -12

p2.x = -2
p2.y = 2

# print(add(p1, p2))
print(add(p2, p2))


@dek(-5, 5)
def sub(p1, p2):
    p = Point()
    p.x = p1.x - p2.x
    p.y = p1.y - p2.y
    return p


# print(sub(p2, p1))
print(sub(p2, p2))


# Zad3


class Zad3():

    @staticmethod
    def count_area(p1, p2, p3, p4=None):
        if p4 is None:
            a = math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
            b = math.sqrt(math.pow(p2.x - p3.x, 2) + math.pow(p2.y - p3.y, 2))
            c = math.sqrt(math.pow(p3.x - p1.x, 2) + math.pow(p3.y - p1.y, 2))
            p = a + b + c
            return math.sqrt(p * (p - a) * (p - b) * (p - c))
        else:
            a = math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
            b = math.sqrt(math.pow(p2.x - p3.x, 2) + math.pow(p2.y - p3.y, 2))
            c = math.sqrt(math.pow(p3.x - p4.x, 2) + math.pow(p3.y - p4.y, 2))
            d = math.sqrt(math.pow(p4.x - p1.x, 2) + math.pow(p4.y - p1.y, 2))
            p = a + b + c + d
            return math.sqrt((p - a) * (p - b) * (p - c) * (p - d))

    @staticmethod
    def count_obwod(p1, p2, p3, p4=None):
        if p4 is None:
            a = math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
            b = math.sqrt(math.pow(p2.x - p3.x, 2) + math.pow(p2.y - p3.y, 2))
            c = math.sqrt(math.pow(p3.x - p1.x, 2) + math.pow(p3.y - p1.y, 2))
            return a + b + c
        else:
            a = math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
            b = math.sqrt(math.pow(p2.x - p3.x, 2) + math.pow(p2.y - p3.y, 2))
            c = math.sqrt(math.pow(p3.x - p4.x, 2) + math.pow(p3.y - p4.y, 2))
            d = math.sqrt(math.pow(p4.x - p1.x, 2) + math.pow(p4.y - p1.y, 2))
            return a + b + c + d


p3 = Point()
p3.x = 1
p3.y = 2
p4 = Point()
p4.x = 50
p4.y = 8

print(Zad3.count_obwod(p1, p2, p3))
print(Zad3.count_obwod(p1, p2, p3, p4))

print(Zad3.count_area(p1, p2, p3))
print(Zad3.count_area(p1, p2, p3, p4))


# Zad4


class Zad4:
    counter = {}

    def __init__(self, fun):
        self.fun = fun
        Zad4.counter[fun] = 0

    def __call__(self, *args, **kwargs):
        Zad4.counter[self.fun] += 1
        self.fun(*args, **kwargs)

    @staticmethod
    def print_counter_static():
        for k, val in Zad4.counter.items():
            print(k, val)

@Zad4
def fun1():
    pass

@Zad4
def fun2():
    pass

@Zad4
def fun3():
    pass


for i in range(120):
    fun1()
    for j in range(2):
        fun2()
        for k in range(9):
            fun3()

print(Zad4.print_counter_static())