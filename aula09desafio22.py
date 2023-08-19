nome = input("Digite o seu nome: ")
nome0 = nome.strip()

print(f'Nome com todas as letras maiúsculas :{nome0.upper()}')

print(f'Nome com todas as letras minúsculas :{nome0.lower()}')

#retirando os espaços da string
nome2 = nome0.replace(' ', '')
print(f'Quantos caracteres o nome tem: {len(nome2)}')

#quebrando a string em varias
nome3 = nome0.split()
print(f'O nome {nome3[0]} tem {len(nome3[0])} letras')


