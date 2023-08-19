matriz = []
soma3col = somapares = cont = maior2col = 0
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input((f'Digite o elemento: [{x}] [{y}]')))
        matriz.append(num)
for linha in range(0, 3):
    for numero in range(0, 3):
        if matriz[cont] % 2 == 0:
            somapares += matriz[cont]
        if numero == 2:
            soma3col += matriz[cont]
        if linha == 1 and matriz[cont] > maior2col:
            maior2col = matriz[cont]
        print(f' [  {matriz[cont]}  ]', end='')
        cont += 1
    print()
print(f'A soma dos numeros pares digitados é: {somapares}')
print(f'A soma da terceira coluna é: {soma3col}')
print(f'O maior valor da segunda linha é:{maior2col}')