pessoas = list()
data = list()
pesados = list()
leves = list()
while True:
    data.append(input("Nome:"))
    data.append(int(input("Peso:")))
    pessoas.append(data[:])
    data.clear()
    continuar = input("Deseja continuar?")
    if continuar.upper() == 'N':
        break

for pessoa in pessoas:
    if pessoa[1] >= 80:
        pesados.append(pessoa[0])
    else:
        leves.append(pessoa[0])

print(f'{len(pessoas)} Pessoas foram entrevistadas')
print(f'As pessoas com mais de 80 kg são: {pesados}')
print(f'As pessoas com menos de 80 kg são: {leves}')