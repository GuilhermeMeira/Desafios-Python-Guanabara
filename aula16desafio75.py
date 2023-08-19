tupla = ()
par = ()
for c in range(0, 4):
    n = int(input('Digite um número:'))
    tupla += (n,)

for num in tupla:
    if num % 2 == 0:
        par += (num,)

print(f'Existem {tupla.count(9)} noves na tupla')
if 3 in tupla:
    print(f'O primeiro 3 for digitado na posição{tupla.index(3) + 1}')
else:
    print('Não existe valor 3 na tupla')

print(f'Os números pares foram {par}')

