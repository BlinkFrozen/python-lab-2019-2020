import abc
import types
import math
from copy import deepcopy
import random
import re


# Zad1

class Calka(abc.ABC):
    def __init__(self, start, stop, number_of_steps, fun):
        if not isinstance(start, (float, int)) or not isinstance(stop, (float, int)):
            raise TypeError("first/second arg is not a number")
        if not isinstance(fun, types.FunctionType):
            raise TypeError("last argument is not a function")
        if not isinstance(number_of_steps, int):
            raise TypeError("number of steps in not int")
        self.start = start
        self.stop = stop
        self.number_of_steps = number_of_steps
        self.fun = fun

    @abc.abstractmethod
    def calculate(self):
        '''
        calculates the integral
        :return: calculated integral
        '''


class CalkaTrapezow(Calka):
    def __init__(self, start, stop, number_of_steps, fun):
        super().__init__(start, stop, number_of_steps, fun)

    def calculate(self):
        '''
        Calculates the integral with trapeze method
        :return: calculated integral
        '''
        step = math.fabs(self.stop - self.start) / self.number_of_steps
        return step / 2 * sum([self.fun(self.start + i * step) + self.fun(self.start + (i + 1) * step) for i in
                               range(self.number_of_steps)])


# print(CalkaTrapezow(0, 1, 100, lambda x: x).calculate())


class WrongValuesException(Exception):
    pass


class NotAFunctionException(Exception):
    pass


class NotANumberException(Exception):
    pass


class CalkaSimpsona(Calka):
    def __init__(self, start, stop, number_of_steps, fun):
        super().__init__(start, stop, number_of_steps, fun)

    def calculate(self):
        h = (self.stop - self.start) / (self.number_of_steps * 2)
        arg = lambda i: self.start + (h * i)
        return (h / 3) * (
                self.fun(arg(0)) + 4 * sum([self.fun(arg(i * 2 + 1)) for i in range(self.number_of_steps)]) + 2 *
                sum([self.fun(arg(i * 2 + 2)) for i in range(self.number_of_steps)]) + self.fun(
            arg(2 * self.number_of_steps)))


# print(CalkaSimpsona(0, 1, 100, lambda x: x).calculate())


# Zad2


class Stos:
    def __init__(self, stos=None):
        if stos is not None and isinstance(stos, Stos):
            self.stos = deepcopy(stos.stos)
        else:
            self.stos = []

    def __len__(self):
        return len(self.stos)

    def __str__(self):
        return str(self.stos)

    def push(self, value):
        self.stos.append(value)

    def pop(self):
        if len(self.stos) > 1:
            value = self.stos[-1]
            del self.stos[-1]
            return value
        else:
            return None

    def add_another_stos(self, sztos):
        value = sztos.pop()
        while value is not None:
            self.push(value)
            value = sztos.pop()


class SortedStos(Stos):

    def __init__(self, stos=None):
        if isinstance(stos, Stos) and sorted(stos.stos) == stos.stos:
            super(SortedStos, self).__init__(stos)
        else:
            super(SortedStos, self).__init__()
    def push(self, value):
        if len(self) > 0:
            if value > self.stos[-1]:
                super(SortedStos, self).push(value)
        else:
            super(SortedStos, self).push(value)



# suma = 0
# for i in range(100):
#     s = SortedStos()
#     for j in range(100):
#         s.push(random.randint(0, 100))
#     suma += len(s)
#
# suma = suma / 100
# print(suma)


# Srednio 4.87

# Zad 3
class WC:
    def __init__(self, file_name):
        self.file_name = file_name

    def calculate(self):
        with open(self.file_name) as file:
            lines = file.readlines()
            lines_amount = len(lines)
            word_amount = 0
            char_amount = 0
            for line in lines:
                char_amount += len(line)
                word_amount += len(re.findall('\w+', str(line)))
            print(lines_amount, word_amount, char_amount)


wc = WC('lorem.txt')

wc.calculate()

