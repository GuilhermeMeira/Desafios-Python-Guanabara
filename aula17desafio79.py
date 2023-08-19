lista = []

while True:
    numero = int(input("Digite um valor: "))
    if numero in lista:
        print("Valor duplicado ! Não vou adicionar")
    else:
        lista.append(numero)
        print(f"O número {numero} foi adicionado à Lista")
    continuar = input("Quer continuar?")
    if continuar.upper() == 'N':
        break

print(f'Você digitou os valores {sorted(lista)}')