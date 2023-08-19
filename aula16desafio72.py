numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze'
           , 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20'))
    while n < 0 or n > 20:
        n = int(input('Tente novamente (0 - 20)'))
    print(numeros[n])
    continuar = input('Deseja continuar? S/N').upper().strip()[0]
    if continuar == 'N':
        break