cidade = str(input("Qual o nome da cidade?"))
cidadesplit = cidade.split()

print(f'Essa cidade começa com santo?{"Santo" in cidadesplit[0].title() }')

