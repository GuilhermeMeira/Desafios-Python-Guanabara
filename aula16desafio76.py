tupla = ('Banana', 5, 'Maçã', 4, 'Computador', 7000, 'Cadeira', 300, 'Mesa', 1000)
tuplanome= ()
tuplapreço = ()
x = 0
# for produto in tupla:
#     if tupla.index(produto) % 2 == 0:
#         tuplanome += (produto,)
#     else:
#         tuplapreço += (produto,)
#
# for x in range(0, len(tuplapreço)):
#     print(f'{tuplanome[x], tuplapreço[x]}')

for produto in tupla:
    if tupla.index(produto) % 2 == 0:
        print(f'{produto:-<30}', end= '')
    else:
        print(f'R${produto:.2f}')