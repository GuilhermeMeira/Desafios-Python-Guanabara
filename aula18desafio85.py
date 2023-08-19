lista = [[], []]

for n in range(0, 7):
    num = int(input("Digite um número"""))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'Todos os números são: {lista}')
print(f'OS NÚMERO IMPARES SÃO: {sorted(lista[1])}')
print(f'OS NÚMEROS PARES SÃO: {sorted(lista[0])}')
