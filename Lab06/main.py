# Zad1
def zad1(filename, n):
    with open(filename, "r") as file:
        data = file.readlines()
        # n first
        print(data[:n])
        # n last
        print(data[-n:])
        # n-th row
        print([data[::n]])
        # n-th word
        print(list(map(lambda line: line.split(' ')[n - 1], data)))
        # n-th char
        print(list(map(lambda line: line[n - 1], data)))


zad1("example.txt", 2)


# Zad2

def zad2():
    from numpy import average, std
    from os import listdir
    x = []
    y = []
    for file in listdir("."):
        if file.startswith('plik') and file.endswith('.in'):
            with open(file) as f:
                data = f.readlines()
                x.append(list(map(lambda line: float(line.split(' ')[0]), data)))
                y.append(list(map(lambda line: float(line.split(' ')[1]), data)))
                print(y)

    with open('plik1.out', 'w') as file:
        for i in range(len(x[0])):
            file.write('{} {} {}\n'.format(average([lista[i] for lista in x]), average([lista[i] for lista in y]),
                                           std([lista[i] for lista in y])))


zad2()


# Zad3s


def zad3():
    files = ['plik1.in', 'plik2.in', 'plik3.in', 'plik4.in', 'plik5.in']
    with open('zad3.out', 'w') as plik:
        plik.write("""files = ['plik1.in','plik2.in','plik3.in','plik4.in','plik5.in']
import matplotlib.pyplot as plt
import numpy
for file in files:
    x, y = numpy.loadtxt(file, unpack=True)
    dy = numpy.std(y)
    plt.plot(x, y, 'o')
    plt.errorbar(x, y, marker='*', yerr=dy)
    plt.savefig('{}.pdf'.format(file.split('.')[0]))
    plt.clf()
""")


zad3()


# Zad4

def zad4():
    from os import listdir
    from re import split
    for file in listdir("."):
        if file.endswith('.py'):
            with open(file) as count:
                data = count.read()
                unique = {}
                # words = data.split()
                import re
                words = re.findall(r'[\w]+', data)
                for x in words:
                    if x not in unique.keys():
                        unique[x] = 1
                    else:
                        unique[x] = unique[x] + 1
                print(unique)


zad4()


# Zad5

def zad5():
    with open('zad5.in') as file:
        data = file.read().splitlines()
        list1 = []
        list2 = []
        for line in data:
            if all(number.isdigit() for number in line.split(' ')):
                list1.append(line.split(' ')[0])
                list2.append(line.split(' ')[1:])
            else:
                list2.extend(line.split(' '))
            print(list1)
            print(list2)


zad5()
