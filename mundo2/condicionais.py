
nome = str(input('Qual é o seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paul':
    print('Seu nome é bem popular no Brasil') # estrutura aninhada
elif nome in 'Anan Claúdia Jéssica e Juliana':
    print('Belo nome feminino')
else:
    print('Sue nome é bem normal')
print('Tenha um bom dia {}'.format(nome))