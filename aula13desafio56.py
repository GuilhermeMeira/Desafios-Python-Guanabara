listanome = []
listaidade = []
listasexo = []
nome = []
maioridade = 0
for c in range(0, 4):
    nome = str(input(f'Digite o {c + 1}ºnome '))
    listanome.append(nome)
    idade = int(input(f'Digite a {c + 1}º idade '))
    listaidade.append(idade)
    sexo = str(input(f'Digite o {c + 1}ºsexo ')).upper()
    if sexo.upper() == "MASCULINO" or sexo.upper() == "FEMININO":
        listasexo.append(sexo)

# média entre as idades do grupo
media = sum(listaidade) / len(listaidade)
print(f'A média de idade do grupo é {media:.2f} anos')

# masculino mais velho
if 'MASCULINO' in listasexo:
    for x in range(0, 4):
        if listasexo[x] == 'MASCULINO' and listaidade[x] > maioridade:
            maioridade = listaidade[x]
            nome = listanome[x]
    print(f'O homem mais velho tem {maioridade} anos e se chama {nome}')
else:
    print('Não existem homens na lista.')

#femininas com menos de 20 anos
contador = 0
for j in range(0, 4):
    if listasexo[j] == 'FEMININO':
        if listaidade[j] < 20:
            contador += 1
print(f'A quantidade de mulheres com menos de 20 anos é: {contador}')


# Encontrando o indice do mais velho e lendo se ele é masculino #essa forma n foi muito boa
#maxindex = (listaidade.index(max(listaidade)))
#if listasexo[maxindex] == 'MASCULINO':
    #print(f'O nome do Homem mais velho é: {listanome[maxindex ]}')
#elif listasexo[maxindex + 1] == 'MASCULINO':
    #print(f'O nome do Homem mais velho é: {listanome[maxindex + 1]}')
#elif listasexo[maxindex + 2] == 'MASCULINO':
    #print(f'O nome do Homem mais velho é: {listanome[maxindex + 2]}')
#elif listasexo[maxindex + 3] == 'MASCULINO':
    #print(f'O nome do Homem mais velho é: {listanome[maxindex + 3]}
# mulheres com menos de 20 anos
