import math
cato = float(input("Digite o comprimento do cateto oposto"))
cata = float(input("Digite o comprimento do cateto adjacente"))

hip = math.sqrt((math.pow(cato, 2) + math.pow(cata, 2)))

#print(math.hypot(cato,cata)) outra forma de escrever - IDEAL

#print(((cato**2) + (cata**2))**(1/2)) outra forma de escrever

print(f'Sabendo que o cateto oposto mede: {cato} e o cateto adjacente mede: {cata} a hipotenusa mede: {hip}')
