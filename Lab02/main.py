# Zad1
def is_prime(number):
    if number > 1:
        for i in range(2, number // 2):
            if (number % i) == 0:
                return False
            break
        return True
    return False


# print(is_prime(11))

# Zad2
import random


s = {}
while len(s) < 50:
    n = random.randrange(0,100)
    s.setdefault(n, is_prime(n))

# print(s)

# Zad3
list11 = [random.randrange(0,11) for i in range(100)]
s = {}
for i in list11:
    s.setdefault(i, []).append(list11.index(i, s[i][-1] + 1 if s[i] else 0))

# print(s)


# Zad4

import sys

if(len(sys.argv) < 2):
    print("Podaj liczbe potrzebna do 4 zadania")
    exit(-1)

value = int(sys.argv[1])
s = {i: random.randrange(2,15) for i in range(value)}
# print(s)
l = [(i, s[i], {s[p]: p for p in range(value)}) for i in range(value)]

# print(l)

# Zad5


list100 = [random.randrange(0,20) for i in range(100)]

even = {}
odd = {}
for i in range(20):
    if i % 2 == 0:
        even.setdefault(i, [l for (l, v) in enumerate(list100) if v == i])
    else:
        odd.setdefault(i, [l for (l, v) in enumerate(list100) if v == i])

# print(even)

even_by_3 = {k : (min(v), max(v)) for k,v in even.items() if True in [i % 3 == 0 for i in v]}
# print(even_by_3)


# Zad 6

dict1 = {k: random.randrange(0,100) for k in range(10)}
dict2 = {k: random.randrange(0,100) for k in range(10)}

dict1reverse = {v:k for k,v in dict1.items()}
dict2reverse = {v:k for k,v in dict2.items()}

# dict_combined = {k[0]: (v,v) for k, v in zip(dict1.items(), dict2.items()) if }
# print(dict_combined)