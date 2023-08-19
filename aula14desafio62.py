pt = int(input('Digite o primeiro termo'))
razao = int(input('Digite a razao'))
termo = pt
contador = 0
termos = 10

while contador != termos :
    if contador == 0:
        print(pt, end= ' ')
        contador += 1
    else:
        termo = termo + razao
        print(termo, end=' ')
        contador +=1
print('PAUSA')
y = 1
while y != 0:
    y = int(input('Quantos termos a mais você quer ver?'))
    while contador != termos + y:
        termo = termo + razao
        print(termo, end=' ')
        contador += 1
    termos = termos + y
print(f'Fim, foram analisados {termos} termos')
