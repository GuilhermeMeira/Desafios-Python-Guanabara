a = float(input('Digite o comprimento do lado do triangulo'))
b = float(input('Digite o comprimento do lado do triangulo'))
c = float(input('Digite o comprimento do lado do triangulo'))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
