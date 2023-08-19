lista = []

for n in range(0, 5):
    num = int(input("Digite um valor: "))
    if n == 0 or num > max(lista) :
        lista.append(num)
        print("Número adicionado ao fim da lista.")
        print(lista)
    else:
        for posicao, num2 in enumerate(lista):
            if num <= num2:
                lista.insert(posicao, num)
                print(lista)
                print(f'Número {num} adicionado na posiçao {posicao}')
                break
print(lista)