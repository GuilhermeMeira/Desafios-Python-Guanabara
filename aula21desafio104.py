def leiaint(a):
    b = input(a)
    while not b.isnumeric():
        b = (input('ERRO! DIGITE UM NUMERO INTEIRO'))
    b = int(b)
    return b


n = leiaint("Digite um número")

print(f'O número digitado foi {n}')