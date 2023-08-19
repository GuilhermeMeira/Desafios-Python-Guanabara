from time import sleep


def fatorial(número, show=True):
    """
    Calcula o fatorial de um número
    :param número: numero a ser calculado
    :param show: Se deve ou não ser mostrado o cálculo
    :return: o valor do fatorial do número
    """
    f = 1
    for i in range(número, 0, -1):
        f = f * i
        if show:
            sleep(0.3)
            if i != 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} =', end=' ')
    return f


print(fatorial(4, False))

print(fatorial(2))

print(fatorial(10))
