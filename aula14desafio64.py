y = 0
soma = 0
contador = 0
while y != 999:
    y = int(input('Digite um número'))
    if y == 999:
        print('Fim')
    else:
        contador += 1
        soma += y
print(f'A soma de todos os números é: {soma}')
print(f'A quantidade de números digitados foi: {contador}')