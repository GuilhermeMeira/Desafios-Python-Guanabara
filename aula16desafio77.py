tupla = ('Banana', 'abacate', 'amora', 'laranja')


for fruta in tupla:
    print(f' Em {fruta} temos:', end=' ')
    for letra in fruta:
        if letra in 'aeiouAEIOU':
            print(letra, end=' ')
    print()


