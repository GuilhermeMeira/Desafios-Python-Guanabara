jogador = {'nome': input("Nome:"),
           'partidas': int(input("Quantas partidas"))
           }
gols = []
for x in range(0, jogador['partidas']):
    gol = int(input(f"Quantos gols na partida {x}"))
    gols.append(gol)
jogador['gols'] = gols
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]}')
for x in range(0, jogador['partidas']):
    print(f'Na partida {x}, fez {jogador["gols"][x]}')
print(f'Foi um total de {sum(jogador["gols"])} gols')
