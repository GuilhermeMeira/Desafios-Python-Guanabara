a = float(input('Digite o comprimento do lado do triangulo'))
b = float(input('Digite o comprimento do lado do triangulo'))
c = float(input('Digite o comprimento do lado do triangulo'))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Com essas medidas é possivel formar um triangulo.', end = '')
    if a == b == c:
        print(' Esse é um triangulo equilátero')
    elif a == b or a == c or b == c:
        print(' Esse é um triangulo isóceles')
    else:
        print(' Esse é um triangulo escaleno')
else:
    print('Não é possível formar um triangulo.')