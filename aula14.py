
valor = 1
par = 0
impar = 0
parar = 'S'
while parar == 'S':
    valor = int(input('Digite o numero secreto'))
    parar = str(input('Deseja continuar? (s/N)')).upper()
    if valor % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Existem {par} números pares e {impar} números impares')