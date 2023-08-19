peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f} (ABAIXO DO PESO)')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f} (PESO IDEAL)')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f} (SOBREPESO)')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f} (OBESIDADE)')
else:
    print(f'Seu IMC é {imc:.1f} (OBESIDADE MÓRBIDA)')
