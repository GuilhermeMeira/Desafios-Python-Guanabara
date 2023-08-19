import random
from time import sleep
lista = []
soma = 0


def sorteia():
    print(f'Sorteando 5 valores da lista ', end='')
    for x in range(0, 5):
        rnd = random.randint(0, 10)
        sleep(0.3)
        print(rnd, end=' ')
        lista.append(rnd)
    print()


def somapar():
    soma = 0
    print(f'Os valores pares de {lista} são: ', end='')
    for num in lista:
        if num % 2 == 0:
            sleep(0.3)
            print(num, end=' ')
            soma += num
    print(f' E a soma deles é: {soma}')


sorteia()
somapar()