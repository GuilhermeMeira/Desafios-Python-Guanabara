parar = 'S'
valor = soma = maxvalor = minvalor = contador = 0
while parar == 'S':
    valor = int(input('DIGITE UM VALOR'))
    if contador == 0:
        maxvalor = valor
        minvalor = valor
    if valor > maxvalor:
        maxvalor = valor
    if valor < minvalor:
        minvalor = valor
    soma += valor
    contador += 1
    parar = input('Deseja continuar? [S/N]').upper()
print(f'A média entre os valores é {soma/ contador}')
print(f'O maior valor lido foi {maxvalor} e o menor foi {minvalor}')
