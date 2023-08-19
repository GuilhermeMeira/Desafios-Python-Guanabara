pt = int(input('Digite o primeiro termo'))
razao = int(input('Digite a razao'))
termo = pt
contador = 0
soma = 0
while contador != 10:
    if contador == 0:
        print(pt, end= ' ')
        contador += 1
    else:
        termo = termo + razao
        pt = termo + pt
        soma += termo
        print(termo, end=' ')
        contador += 1
