from time import sleep
def contador():
    print('-' * 20)
    print(f'Contagem de 1 a 10')
    print('-' * 20)
    for x in range(1, 11):
        print(x, end=' ')
        sleep(0.25)
    print()
    print('-' * 20)
    print(f'Contagem de 10 até 0 (-2)')
    print('-' * 20)
    for y in range(10, -1, -2):
        print(y, end=' ')
        sleep(0.25)
    print(f'Contagem personalizada !!')
    início = int(input("Início:"))
    fim = int(input("Fim:"))
    passo = int(input("Passo:"))
    if início > fim:
        if passo < 0:
            passo = passo
        else:
            passo = passo * -1
    elif fim > início:
        if passo > 0:
            passo = passo
        else:
            passo = passo *-1
    if passo > 0:
        for z in range(início, fim + 1, passo):
            print(z, end=' ')
            sleep(0.25)
    else:
        for z in range(início, fim - 1, passo):
            print(z, end=' ')
            sleep(0.25)

contador()