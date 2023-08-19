
p = float(input('Qual o preço do produto?'))

d = float(input('Qual desconto você recebeu em %'))

pf = p - (p*d/100)

print(f'O preço com desconto é : {pf:.2f}!')

