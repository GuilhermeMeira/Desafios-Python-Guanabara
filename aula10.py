n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/ 2

if m >= 6:
    print(f'Parabens!! sua média é: {m}')
else:
    print(f'Sua média é: {m} Que pena :(')

print(f'Parabens!! sua média é {m}'if m >= 6 else print(f'Sua média é: {m} Que pena :('))
