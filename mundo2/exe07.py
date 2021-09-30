from datetime import date
ano_atual = date.today().year
print('--------------------------------------------')
ano_nasc = int(input('Digite o ano de nascimento: '))

idade = ano_atual - ano_nasc

if (idade >= 9) and (idade < 14):
    categoria = 'Mirim'
    print('Você possui {} anos de acorde com a sua idade voce está na categoria {}'.format(idade, categoria))
elif (idade >= 14) and (idade < 19):
    categoria = 'Infantil'
    print('Você possui {} anos de acorde com a sua idade voce está na categoria {}'.format(idade, categoria))
elif (idade >= 19) and (idade <= 25):
    categoria = 'Senior'
    print('Você possui {} anos de acorde com a sua idade voce está na categoria {}'.format(idade, categoria))
elif idade > 25:
    categoria = 'Master'
    print('Você possui {} anos de acorde com a sua idade voce está na categoria {}'.format(idade, categoria))
else:
    saldo = 9 - idade
    print('>> Você tem {} anos a idade miníma é a partir de 9, tente se escrever novamente daqui a {} anos.'.format(idade,saldo))



