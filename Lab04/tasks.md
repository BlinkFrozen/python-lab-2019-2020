1. Proszę napisać program testujący alternatywne sposoby budowania zestawu wartości: pętla for, lista składana, funkcja map i wyrażenie generatorowe (składnia taka jak listy składanej tylko w miejsce nawiasów kwadratowych należy wstawić okrągłe; o generatorach będziemy mówić na kolejnych zajęciach). Dla każdego ze sposobów proszę utworzyć osobną funkcję tak, aby uzupełnić poniższy kod:

    import time
    import sys
    
    powt=1000
    N=10000
    (...)
    print(sys.version)
    test=(forStatement, listComprehension, mapFunction, generatorExpression)
    for testFunction in test:
        print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
    
    gdzie: tester - funkcja wywołująca powt razy daną funkcję, w której tworzonych jest N wartości.

Proszę wykonać testy (wszystko w ramach tych samych funkcji):
        dodawanie elementu
        dodawanie elementu podniesionego do kwadratu
        sumowanie elementów z wykorzystaniem pętli for
        sumowanie z wykorzystaniem funkcji sum
        konwersja obiektu map i generatora do listy

Do pomiaru czasu proszę użyć funkcji time_ns z modułu time. Otrzymane wyniki proszę dołączyć do wysyłanego programu (2p)

2. Proszę utworzyć dwie listy po sto wartości losowych z przedziału [0,20) każda. Następnie na ich podstawie proszę utworzyć listę dwuelementowych krotek, elementów o jednakowych indeksach w listach wyjściowych spełniających warunek, że suma ich wartości jest większa od 3 i mniejsza od 15. Należy wykorzystać listę składaną oraz funkcje filter i zip (2p)

3. Proszę napisać funkcję przyjmującą dwa parametry - lista x-ów i y-ów. Korzystając z funkcji wbudowanych sum i map proszę obliczyć (i zwrócić z funkcji) wartości dofitowanych współczynników prostej oraz ich niepewności (wzory w pliku) (2p).

4. Proszę napisać funkcję myreduce przyjmującą dwa parametry (funkcję i sekwencję) oraz zwracającą liczbę. Funkcja przekazywana jako parametr będzie funkcją przyjmującą dwa parametry. Działanie funkcji proszę przetestować korzystając z wyrażenia lambda dla dodawania i mnożenia (2p)

5. Mamy listę, której elementami są listy dwuelementowe (możemy je potraktować jako współrzędne punktów na płaszczyźnie). Chcemy utworzyć nową listę, w której pierwszym elementem jest lista x-ów, a drugim lista y-ów. Proszę to zrobić w jednej linijce korzystając z funkcji myreduce, wyrażenia lambda oraz wbudowanej funkcji map (obie listy tworzymy jednocześnie!) (2p)