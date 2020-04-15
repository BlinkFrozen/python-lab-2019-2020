# Zad1

from math import log
import random


def infinite():
    i = -1
    while True:
        i += 1
        yield i


def perfect(seq):
    for number in seq:
        sum = 0
        for i in range(1, number // 2 + 1):
            if (number % i) == 0:
                sum += i
        if number == sum:
            yield number


# print([i for i in perfect([1 ,2 ,3, 6, 28])])


def until_bigger(seq, blocker):
    for i in seq:
        if i < blocker:
            yield i
        else:
            break


# print([i for i in until_bigger([2,1,3,4,5,6], 5)])


# for i in perfect(until_bigger(infinite(), 10000)):
#     print(i)


# Zad2
def zad2():
    u0 = 0
    x0 = 1
    a = 0.05
    x = x0
    uj = u0
    for l in infinite():
        uj = uj + (a / x)
        if x <= 1.5:
            yield x, uj, log(x)
            x = x0 + (l * a)
        else:
            break


# for i in zad2():
#     print(i)

# Zad 3


# Zad4

def zad4():
    x0 = random.random()
    while True:
        x = random.random()
        if x < 0.1:
            return
        elif x - 0.4 < x0 > x + 0.4:
            yield x
        x0 = x


# for i in zad4():
#     print(i)


# Zad5

def my_range(start=0, stop=None, step=1):
    if stop is None:
        if start < 0:
            return
        stop, start = start, 0
    elif stop < start and step >= 0:
        return
    elif stop > start and step <= 0:
        return

    if stop < start:
        if step < 0:
            while stop  < start:
                yield start
                # print( stop - step)
                # print(start)
                start = start + step
        else:
            while stop - step < start:
                yield start
                # print( stop - step)
                # print(start)
                start = start + step


    else:
        while stop > start:
            yield start
            start = start + step



for i in range(8):
    print('range: {}'.format(i))

for i in my_range(8):
    print('my range: {}'.format(i))
