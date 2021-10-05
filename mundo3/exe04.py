from datetime import datetime
dados = dict()

dados['nome'] = str(input('Digite o seu nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano_nasc

dados['ctps'] = int(input('digite o número da carteira de trabalho se não tiver o valor é: 0: '))

if dados['ctps'] != 0:
    dados['ano_contratacao'] = int(input('Digite o ano da contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['ano_contratacao'] + 35 - datetime.now().year)

for c,v in dados.items():
    print(f' {c} o valor é {v}')