n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f' O primeiro valor: {n1} é o maior número. ')
elif n2 > n1:
    print(f'O segundo valor: {n2} é o maior número.')
else:
    print('Os dois valores são iguais.')
