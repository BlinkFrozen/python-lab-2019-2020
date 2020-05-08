import numpy as np

l1 = [
    1, 2, 2, 3, 2, 3, 6, 7, 1, 4, 8, 9, 4, 4, 7, 9, 2, 6, 9, 13, 6, 6, 7, 11, 3, 4, 12, 13, 2, 5, 14, 15, 2, 10, 11, 15,
    1,
    12, 12, 17, 8, 9, 12, 17, 1, 6, 18, 19, 6, 6, 17, 19, 6, 10, 15, 21, 4, 5, 20, 21, 4, 8, 19, 21, 4, 13, 16, 21, 8,
    11,
    16, 21, 3, 6, 22, 23, 3, 13, 18, 23, 6, 13, 18, 23, 9, 14, 20, 25, 12, 15, 16, 25, 2, 7, 26, 27, 2, 10, 25, 27, 2,
    14,
    23, 27, 7, 14, 22, 27, 10, 10, 23, 27, 3, 16, 24, 29, 11, 12, 24, 29, 12, 16, 21, 29, 2]

l2 = [
    1, 2, 2, 3, 2, 3, 6, 7, 1, 4, 8, 9, 4, 4, 7, 9, 2, 6, 9, 13, 6, 6, 7, 11, 3, 4, 12, 13, 2, 5, 14, 15, 2, 10, 11, 15,
    1,
    12, 12, 17, 8, 9, 12, 17, 1, 6, 18, 19, 6, 6, 17, 19, 6, 10, 15, 21, 4, 5, 20, 21, 4, 8, 19, 21, 4, 13, 16, 21, 8,
    11,
    16, 21, 3, 6, 22, 23, 3, 13, 18, 23, 6, 13, 18, 23, 9, 14, 20, 25, 12, 15, 16, 25, 2, 7, 26, 27, 2, 10, 25, 27, 2,
    14,
    23, 27, 7, 14, 22, 27, 10, 10, 23, 27, 3, 16, 24, 29, 11, 12, 24, 29, 12, 16, 21, 29]

l3 = [3, 4, 5, 5, 12, 13, 7, 24, 25, 9, 40, 41, 6, 8, 10, 60, 80, 100, 18, 24, 30, 15, 8, 17]

l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Zad1

class WrongListLength(Exception):
    pass


class NotASinglePythagorasN(Exception):
    pass


def zad1(l, n):
    if len(l) % n != 0:
        raise WrongListLength
    amount_of_pythagoras_n = 0
    for i in range(0, len(l) - 1, n):
        if sum([value ** 2 for value in l[i: i + n - 1]]) == l[i + n - 1] ** 2:
            odd = []
            even = []
            [even.append(l[value]) if l[value] % 2 == 0 else odd.append(l[value]) for value in range(i, i + n) ]
            amount_of_pythagoras_n = amount_of_pythagoras_n + 1
            print("odd:{} even:{} in {}".format(odd, even,l[i:i + n]))
    if amount_of_pythagoras_n == 0:
        raise NotASinglePythagorasN
    print(amount_of_pythagoras_n)


zad1(l3, 3)


# Zad2

class NotANumberException(Exception):
    pass


class NotSortedException(Exception):
    pass


def zad2(n_values):
    for i in range(len(n_values)):
        if not isinstance(n_values[i], int) and not isinstance(n_values[i], float):
            raise NotANumberException
    if not sorted(n_values):
        raise NotSortedException
    n = len(n_values) - 1
    return n_values[-1] - n_values[0], n_values[
        (n + 1) // 2] if n % 2 != 0 else (n_values[n // 2] + n_values[(n // 2) + 1]) / 2


print(zad2([1, 2, 3, 4]))


# Zad3
class WrongValuesException(Exception):
    pass


class NotAFunctionException(Exception):
    pass


def zad3(f, borders, n_partitions):
    assert (callable(f))
    if isinstance(borders, tuple()):
        if isinstance(borders[0], int) and isinstance(borders[1], int) or isinstance(borders[0], float) or isinstance(
                borders[1], float):
            if borders[1] < borders[0]:
                raise WrongValuesException
            else:
                if isinstance(n_partitions, int):
                    pass
                else:
                    raise NotANumberException
        else:
            raise NotANumberException
    h = (borders[1] - borders[0]) / (n_partitions * 2)
    arg = lambda i: borders[0] + (h * i)
    return (h / 3) * (f(arg(0)) + 4 * sum([f(arg(i * 2 + 1)) for i in range(n_partitions)]) + 2 *
                      sum([f(arg(i * 2 + 2)) for i in range(n_partitions)]) + f(arg(2 * n_partitions)))


# print(zad3(lambda x: x, (0, 1), 1))


# Zad4
class NoZeroException(Exception):
    pass


class FunctionNotOkreslonaInPoint(Exception):
    pass


def zad4(f, borders, epsilon=10 ** -7):
    a = borders[0]
    b = borders[1]
    if f(a) * f(b) > 0:
        raise FunctionNotOkreslonaInPoint
    while abs(b - a) > epsilon:
        x = (a + b) / 2
        if abs(f(x)) <= epsilon:
            break
        elif f(x) * f(a) < 0:
            b = x
        else:
            a = x
    else:
        raise NoZeroException
    print((a + b) / 2)


# zad4(lambda x: x + 1, [-2, 0])
# zad4(lambda x: x + 1, [1, 2])
# zad4(lambda x: (x - 2) * (x - 2) / (x - 1) - 2, [0, 2])
# zad4(lambda x: (x - 2) * (x - 2) / (x - 1) - 2, [4, 6])
