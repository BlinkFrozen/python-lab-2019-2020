import random


# Zad1


def zad1(function):
    s = {}
    length = random.randrange(20)
    while len(s) < length:
        x = random.random()
        s['{:.3}'.format(x)] = '{:.3f}'.format(eval(function))
    return s


dict1 = zad1('12 + x')


print('zad1 : ' + str(dict1))


# Zad2


def zad2(*args):
    return_list = []
    for elem in args[0]:
        for l in args:
            if elem not in l:
                break
        else:
            return_list.append(elem)
    return return_list


zad2result = zad2([1, 2, 3], (1, 2), (1, 3))

print('zad2 : ' + str(zad2result))


# Zad3

def zad3(list1, list2, complete_with_none=True):
    if complete_with_none:
        return [(list1[i], list2[i]) for i in range(min(len(list1), len(list2)))]
    else:
        return [(list1[i] if i < len(list1) else None, list2[i] if i < len(list2) else None) for i in
                range(max(len(list1), len(list2)))]


print('zad3 : ' + str(zad3((1, 2, 3), (4, 3, 2, 1))))


# Zad4

def zad4_min(*args):
    return min(*args[0])


def zad4_fun(fun, *args):
    return fun(args)


print(zad4_fun(zad4_min, [4, 5, 0, -12]))


# Zad5

def zad5(amount, coins=(10, 5, 2)):
    original_amount = amount
    r = []
    for i in coins:
        while amount >= i:
            amount = amount - i
            r.append(i)
    return r if amount == 0 else f'Tymi nominałami {coins} i tym algorytmem nie da się rozmienić {original_amount}'


print(zad5(21))


# Zad6

def zad6(number, min_range, max_range, method='r'):
    if method == 'r':
        guess = random.randint(min_range, max_range)
        new_min, new_max = min_range, max_range
        shots = 1
        while guess != number:
            new_min, new_max,shots = (new_min, guess, shots+1) if guess > number else (guess, new_max,shots+1)
            print('shot : ' + str(shots) + ' : ' + str(guess))
            print('range: ' + str(new_min) + ' : ' + str(new_max))
            guess = random.randint(new_min, new_max)
    else:
        new_min, new_max = (min_range, (max_range + min_range) // 2) if number < (max_range + min_range) // 2 else (
        (max_range + min_range) // 2, max_range)
        shots = 1
        while new_min != number or new_max != number:
            new_min, new_max, shots = (new_min, (new_max + new_min) // 2, shots + 1) if number <= (new_max + new_min) // 2 else (
            (new_max + new_min) // 2 + 1, new_max, shots + 1)
            print('shot : ' + str(shots))
            print('range: ' + str(new_min) + ' : ' + str(new_max))
    return (shots)


zad6(18, 0, 100, 'c')
