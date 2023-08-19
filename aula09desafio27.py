nome = str(input("Digite o seu nome completo: "))

nome1 = nome.split()

tamanho = (len(nome1))

print(f'O seu nome completo é {nome}')

print(f'O seu primeiro nome é {nome1[0]}')

print(f'O seu último nome é {nome1[tamanho - 1]}') #a contagem começa em 0 entao tamanho = indice do ultimo - 1


