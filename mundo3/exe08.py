from datetime import date

def Voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        return f'com {idade} anos: NÃO VOTA'
    elif idade >= 18 and idade <= 69:
        return f'com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 70:
        return f'com {idade} anos: VOTO OPCIONAL'
    else:
        return f'com VOTO INVÁLIDO'

print(Voto(2005))
 