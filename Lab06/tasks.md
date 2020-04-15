1. pposzę napisać funkcję, która pozwoli na wypisanie: n początkowych wierszy pliku, n końcowych wierszy pliku, co n-tego wiersza pliku, n-tego słowa ze wszystkich wierszy i n-tego znaku ze wszystkich wierszy. Nazwę pliku oraz n przekazujemy jako parametr do funkcji. Każdy podpunkt==jedna linia kodu (1.5p).

2. Wszystkie pliki z rozszerzeniem in w katalogu bieżącym traktujemy jako wyniki kolejnych serii pomiarów tych samych wielkości. Zakładamy, że w każdym z plików mamy dwie kolumny liczb (x, y). Na wyjściu chcemy otrzymać jeden plik z trzema kolumnami:
        
    - średnia x z danego wiersza ze wszystkich plików (numpy.average),  
    - średnia y z danego wiersza ze wszystkich plików,
    - odchylenie standardowe y z danego wiersza ze wszystkich plików (numpy.std)
 
PLIKI TESTOWE: pliki.zip
 (2p).

3. Proszę napisać funkcję, tworzącą plik z instrukcjami pozwalającymi na wygenerowanie wykresu plików j.w. + wynikowego (łącznie z odchyleniem standardowym)*patrz niżej, proszę skorzystać z potrójnego cudzysłowu (1.5p).

4. Proszę sporządzić histogram słów (należy uwzględnić białe znaki, przecinki, dwukropki, nawiasy, etc.) ze wszystkich plików z określonym rozszerzeniem np. py w katalogu bieżącym (2.5p).

5. Proszę napisać funkcję, która zakładając, że w pliku znajdują się tylko wartości liczbowe, a w poszczególnych wierszach liczba kolumn może być różna, tworzymy dwie listy: do pierwszej trafiają wartości z pierwszej kolumny pod warunkiem, ze wszystkie wartości w danym wierszu konwertują się do wartości całkowitych, do drugiej natomiast wartości z pozostałych kolumn niezależnie od ich typu i liczby (2.5p).
PLIK TESTOWy: zad5.in
* Matplotlib jest biblioteką do tworzenia wykresów (https://matplotlib.org/). Wykorzystamy ją do wygenerowania prostego wykresu. Poniżej minimum konieczne, aby ten cel osiągnąć:

import matplotlib.pyplot as plt
#wyrysowanie krzywej y(x), 'o' oznacza styl punktu
plt.plot(x, y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
plt.errorbar(x, y, marker='*', yerr=dy)
#opis osi
plt.xlabel('x')
#zapis do pliku, format określony przez rozszerzenie w nazwie
plt.savefig('res.pdf')

A to może się przydać do łatwego wczytywania plików (ale dzisiaj można z tego skorzystać tylko w skrypcie generującym wykresy)

import numpy
x,y=numpy.loadtxt(nazwa, unpack=True)