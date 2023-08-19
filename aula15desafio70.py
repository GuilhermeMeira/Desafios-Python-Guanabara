nome = continuar = nomebarato = ''
preco = total = cont = barato = 0
while True:
    if barato == 0:
        nomebarato = nome
        barato = preco
    if continuar == 'N':
        break
    continuar = ''
    nome = input('Digite o nome do produto !')
    preco = int(input('Digite o preço do produto ! '))
    total += preco
    if preco > 1000:
        cont +=1
    if preco < barato:
        barato = preco
        nomebarato = nome
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar? S/N').upper()[0]
print(f'O total gasto foi de R${total}')
print(f'{cont} produtos custam mais que R$1000')
print(f'O produto mais barato é o {nomebarato} custando {barato}')