n1 = int(input('Digite um número'))
n2 = int(input('Digite um número'))
n3 = int(input('Digite um número'))

if n1 > n2 and n1 > n3:
    print(f'{n1} É o maior número')
if n2 > n1 and n2 > n3:
    print(f'{n2} É o maior número')
if n3 > n2 and n3 > n1:
    print(f'{n3} É o maior número')

if n1 < n2 and n1 < n3:
    print(f'{n1} É o menor número')
if n2 < n1 and n2 < n3:
    print(f'{n2} É o menor número')
if n3 < n1 and n3 < n2:
    print(f'{n3} É o menor número')


#outra forma

maior = max(n1,n2,n3)
menor = min(n1,n2,n3)

print(f'O maior número é {maior} e o menor é {menor}')