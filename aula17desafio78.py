lista = []
for i in range(0, 5):
    lista.append(int(input(f"{i} Digite um número: ")))

maior = max(lista)
menor = min(lista)

# print(f'O maior valor da lista é {maior} na posição {lista.index(maior) + 1}')
# print(f'O menor valor da lista é {menor} na posição {lista.index(menor) + 1}')

print(f'O maior valor da lista é {maior} na posição', end=' ')
for posicao, num in enumerate(lista):
    if num == maior:
        print(posicao, end=' ')
print()

print(f'O menor valor da lista é {menor} na posição', end=' ')
for posicao, num in enumerate(lista):
    if num == menor:
        print(posicao, end=' ')
