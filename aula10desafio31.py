d = int(input("Qual a distância da viagem?"))
cores = {'azul' : '\033[34m',
         'roxo' : '\033[35m'}

if d <= 200:
    print(f'O preço da viagem será: R$ \033[34m{d*0.5:.2f}')
else:
    print(f'O preço da viagem será: R$ {d*0.45:.2f}')
