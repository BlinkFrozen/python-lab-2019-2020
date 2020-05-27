# path.append('build/lib.macosx-10.14-x86_64-3.7')

import mod
import random
import time

print(mod.met(1, 2))
print(mod.met(1, 2, 3))
print(mod.met(1, 2, 3, [2, 3, 4]))




 # Zad2
def zad2(n):
    a = [0 for i in range(10)]
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x < 0.1 and y < 0.1:
            a[0] += 1
        elif x < 0.2 and y < 0.2:
            a[1] += 1
        elif x < 0.3 and y < 0.3:
            a[2] += 1
        elif x < 0.4 and y < 0.4:
            a[3] += 1
        elif x < 0.5 and y < 0.5:
            a[4] += 1
        elif x < 0.6 and y < 0.6:
            a[5] += 1
        elif x < 0.7 and y < 0.7:
            a[6] += 1
        elif x < 0.8 and y < 0.8:
            a[7] += 1
        elif x < 0.9 and y < 0.9:
            a[8] += 1
        else:
            a[9] += 1
    return list(map(lambda x: x / n * 100, a))

for value in [10**2, 10**3, 10**4, 10**5, 10**6]:
    print("time c {}:".format(value))
    ti = time.time_ns()
    print(mod.zad2(value))
    print(time.time_ns() - ti)

    print("time python {}:".format(value))
    ti = time.time_ns()
    print(zad2(value))
    print(time.time_ns() - ti)
    print()


# Zad 3

print(mod.zad3({random.randrange(10,100): random.randrange(10,100) for i in range(20)}))


