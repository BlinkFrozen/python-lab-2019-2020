1. Proszę napisać trzy funkcje generatorowe:
    - zwracającą kolejną liczbę naturalną (nieskończony),
    - zwracającą te wartości z przekazanej jako parametr sekwencji, które są liczbami doskonałymi (liczby naturalne, która są sumą wszystkich swoich dzielników właściwych)
    - zwracającą wartości z przekazanej jako pierwszy parametr sekwencji i przerywającą działanie po napotkaniu wartości większej niż drugi parametr przekazany do funkcji                    

Korzystając ze zdefiniowanych funkcji proszę wypisać doskonałe liczby naturalne mniejsze od 10000 (2p)


2. Proszę napisać generator obliczający ui wg zależności:
ui=ui-1+a/xi-1, z wartością początkową u0=0 dla x0=1 oraz z xi=x0+ia
Obliczenia proszę wykonać dla a=0.05 i przerwać je dla x=1.5. Zależność pozwala na wyznaczenie przybliżonej wartości logarytmu naturalnego z danej liczby. Generator ma zwracać x oraz przybliżoną i dokładną wartość logarytmu naturalnego (2p)

3. Każdą liczbę całkowitą można zapisać jako sumę wartości całkowitych mniejszych od niej samej, np. 4 można zapisać jako: 1+1+1+1, 1+1+2, 1+3 oraz 2+2. Proszę napisać generator zwracający wszystkie możliwe sumy dla określonej wartości n (2p)

              
4. Proszę napisać generator zwracający liczby spełniające warunek, że wartość kolejna jest co najmniej o 0.4 mniejsza lub większa od wartości poprzedniej. Działanie generatora należy zakończyć, jeżeli wylosowana wartość jest mniejsza od 0.1 (2p)

5. Proszę napisać generator działający dokładnie tak samo jak wbudowany range (proszę się upewnić, że wiecie Państwo jak on działa!), ale pozwalający na generowanie liczb rzeczywistych (2p)
Do testów: range(8), range(-8), range(1,8), range(8,1), range(1,8,2), range(1,8,-2), range(8,1,2), range(8,1,-2)