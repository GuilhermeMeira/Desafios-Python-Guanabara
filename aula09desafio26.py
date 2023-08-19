frase = str(input("Digite uma frase:")).strip()

a = frase.upper().count("A")

print(f'A letra "A" aparece {a} vez(es) na frase')

print(f'A primeira letra "A" aparece na posição {frase.upper().find("A") + 1}')

print(f'A última letra "A" aparece na posição {frase.upper().rfind("A") + 1}')




