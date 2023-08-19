try:
    a = int(input('numerador'))
    b = int(input('denominador'))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado inserido')
except ZeroDivisionError:
    print('Não é possível dividir por 0 ')
else:
    print(r)
finally:
    print('Fim do programa')