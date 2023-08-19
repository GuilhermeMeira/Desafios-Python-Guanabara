import math

num = float(input('Qual o angulo?'))

seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))

print(f'Do angulo:{num:.2f}° \nO seno é: {seno:.2f} \nO cosseno é: {cos:.2f} \nA tangente é: {tan:.2f}')

#math.radians(num) considera o numero em graus para fazer o calculo
#seno = math.sin(num) #pega o seno de um angulo em radianos
#senor = math.degrees(num) #transforma radianos em graus



