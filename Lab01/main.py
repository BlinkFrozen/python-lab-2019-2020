#!/usr/bin/python3

import sys

# cw1
if (len(sys.argv) < 2):
    print("Powinienen wywołać program z podanien argumentow tego wymaga cwiczenie")
    exit(-1)

cw1 = ''.join(sys.argv[1:])
print(cw1)

# cw2

lower = [smallletter for smallletter in cw1 if smallletter.islower()]
upper = [smallletter for smallletter in cw1 if smallletter.isupper()]
numbers = [smallletter for smallletter in cw1 if smallletter.isnumeric()]
everything_but_a_number = [smallletter for smallletter in cw1 if not smallletter.isnumeric()]

print("lower : " + str(lower))
print("upper : " + str(upper))
print("numbers : " + str(numbers))
print("everything_but_a_number : " + str(everything_but_a_number))

# cw3
lower_without_duplicates = list()
for letter in lower:
    if letter not in lower_without_duplicates:
        lower_without_duplicates.append(letter)

print(lower_without_duplicates)

lower_with_count = [(letter, lower.count(letter)) for letter in lower_without_duplicates]
print(lower_with_count)
#cw4
lower_with_count.sort(key=lambda x: x[1])
print(lower_with_count)

# cw5
vowels = ('a', 'e', 'i', 'j', 'o', 'u', 'A', 'E', 'I', 'J', 'O', 'U')
vowel = [letter for letter in cw1 if letter in vowels]
count_vowel = len(vowel)
consonant_count = len(everything_but_a_number)

print(count_vowel)
print(consonant_count)

cw4 = [(int(letter), (count_vowel * int(letter) + consonant_count)) for letter in numbers]
print(cw4)

cw4.sort(key=lambda x: x[0])
print("cw4.sort : ",cw4)

#cw5
x_z_daszkiem = sum([x[0] for x in cw4]) / len(cw4)
y_z_daszkiem = sum([x[1] for x in cw4]) / len(cw4)
print(x_z_daszkiem)

D = sum([(x - x_z_daszkiem) ** 2 for (x,y) in cw4])
print(D)

a = (1 / D) * sum([y * (x - x_z_daszkiem) for (x,y) in cw4])
b = y_z_daszkiem - a * x_z_daszkiem
print(a)