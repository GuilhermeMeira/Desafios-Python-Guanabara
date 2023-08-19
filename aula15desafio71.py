valor = resto = int(input('Valor a ser sacado:'))
cedula50 = cedula20 = cedula10 = cedula1 = 0
while True:
    cedula50 = valor // 50
    resto = valor % 50
    if cedula50 >= 1:
        print(f'{cedula50} CÉDULAS DE R$50')
    if resto == 0:
        break
    cedula20 = resto // 20
    resto = resto % 20
    if cedula20 >= 1:
        print(f'{cedula20} CÉDULAS DE R$20')
    if resto == 0:
        break
    cedula10 = resto // 10
    resto = resto % 10
    if cedula10 >= 1:
        print(f'{cedula10} CÉDULAS DE R$10')
    if resto == 0:
        break
    cedula1 = resto // 1
    resto = resto % 10
    if cedula1 >= 1:
        print(f'{cedula1} CÉDULAS DE R$1')
    if resto == 0:
        break

