n = 0
while True:
    x = int(input('Qual tabuada deseja ver? (Número negativo para parar)'))
    if x < 0:
        break
    while n <= 10:
        print(f'{x}X{n} = {x*n}')
        n +=1
    n = 0
    