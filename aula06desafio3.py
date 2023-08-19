n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro numero'))
s = n1 + n2

print('A soma entre {} e {} é {}' .format(n1, n2, s))
#ou
print('A some entre', n1, 'e', n2, 'é', s)
#ou(melhor forma)
print(f'A soma entre {n1} e {n2} é {s}')
