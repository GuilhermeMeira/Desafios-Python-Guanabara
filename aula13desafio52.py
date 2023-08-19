n = int(input('Digite um número inteiro'))
s = 0

for c in range(1, n + 1):
    if n % c == 0:
        s += 1  # contador de divisoes inteiras
        print(f'\033[1;32m {c}\033[m', end='')
    else:
        print(f'\033[31m {c}\033[m', end='')


if s == 2: # se for == 2 entao é divisivel por 1 e ele mesmo logo é primo
    print('\033[1;32m\n Esse é um número primo')
else:
    print(f'\n \033[1;36mEsse não é um número primo pois foi divisível por {s} números diferentes')

