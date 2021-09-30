from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite o seu ano de nascimento: '))

idade = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 -idade
    ano = ano_atual + saldo
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento!')
    print('Seu alistamento será em: '.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = ano_atual - saldo
    print('Seu alistamento foi em: {}'.format(ano))
    print('Você já deveria ter se alistado há tantos {} anos.!'.format(saldo))