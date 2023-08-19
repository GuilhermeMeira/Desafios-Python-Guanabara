lista = []

while True:
    lista.append(int(input("Digite um número: ")))
    continuar = input("Deseja continuar?")
    if continuar.upper() == 'N':
        print("Fim do programa.")
        break

print(f' Foram digitados {len(lista)} números.')

print(sorted(lista, reverse=True))

if 5 in lista:
    print('O valor 5 está na lista. Na posição: ', end='')
    for p, num in enumerate(lista):
        if num == 5:
            print(p, end=' ')
else:
    print('O valor 5 não está na lista.')