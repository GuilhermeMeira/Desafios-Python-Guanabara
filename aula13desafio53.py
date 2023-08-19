frase = str(input('Digite uma palavra'))
fraset = frase.replace(' ', '').upper()
fraseinversa = (fraset[(len(fraset)-1)::-1]) # lendo a frase ao contrario ( começando pelo indice da
fraseinversa2 = frase[::-1]                 # ultima letra e diminuindo 1 por 1
if fraset == fraseinversa:
    print('Isso é um palíndromo')
else:
    print('Isso não é um palíndromo')

print(f' O inverso de {frase} é {fraseinversa2}')