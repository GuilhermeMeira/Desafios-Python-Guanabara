matriz = []

cont = 0
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input((f'Digite o elemento: [{x}] [{y}]')))
        matriz.append(num)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f' [  {matriz[cont]}  ]', end='')
        cont += 1
    print()