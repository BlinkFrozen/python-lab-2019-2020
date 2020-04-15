import math

print('Hello World')

a = 3
print(type(a))
b = '4'
print(type(b))
c = "12"
print(type(c))
d = 7.232
print(type(d))
dd = [21]
print("dd : " + str(type(dd)))


f = (2, 3)

g, *h = 1, 23, 4, 5, 6

print(type(f))

print(1 / 2)
print(1 // 2)

print(dir(math))

print(type((1,)))
k = [[1, 2, 3], 4, 5, 6, 7, 8]
k1 = k

k1[0] = '0'
print(k)

k2 = k

k2[0] = 'a'

print(k)

k = [[0]] * 10

k[5].append(1)
print(k)

# lista składana

k = [[] for _ in range(1000)]  # stworzy 1000 obiektow a nie 1000 referencji

k[53].append([3, 4, 5])
k[54].extend([1, 2, 3])
print(k)

l = 12 if True else 'op'

import sys

print(type(sys.argv))

for i in range(12):
    if i > 50:
        break
else: # else sie wykona jesli break sie nie wykona
    print("??")


from datetime import datetime

partition = datetime.now()
time = partition.strftime("%Y-%m-%d")

print(time)


tup = (9,9)
tup = tup + (8,)

print(str(tup) + str(type(tup)))

lit = [1,2,3,4]

print(lit[3:1:-1])