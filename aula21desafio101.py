
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18:
        return f'Com idade {idade} Voto obrigatório'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com idade {idade} Opcional'
    else:
        return f'Com idade {idade} NEGADO'


print(voto(2000))