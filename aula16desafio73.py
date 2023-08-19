times = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Athletico Paranaense', 'Santos', 'São Paulo', 'Internacional', 'Fluminense',
'Corinthians', 'Fortaleza', 'Bahia', 'Ceará', 'Cruzeiro', 'América Mineiro ', 'Atlético Goianiense', 'Chapecoense', 'Botafogo', 'Vasco da Gama', 'Red Bull Bragantino')


print(times[0:5]) #5 primeiros times
print(times[-4:]) # 4 ultimos
print(sorted(times)) #ordem alfabética
print(times.index('Chapecoense') + 1) # colocaçao do chapecoense (+1 pq a tupla começa em 0)