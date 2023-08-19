dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram rodados?'))

preço = (dias*60) + (0.15*km)

print(f'O preço final com {dias} dias alugados e {km}km rodados é de R${preço:.2f}')


