''' Crie um programa que leia nome,sexo
e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário  e todos os dicionarios em uma lista e mostre
a mesma no final
'''
data = dict()
lista = list()
soma = 0
mulheres = 0
quant_pessoas = int(input('Quantidade de pessoas a serem analisadas: '))

for i in range(0, quant_pessoas):
    data.clear()
    data['nome'] = str(input('Nome: '))
    while True:
        data['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if data['sexo'] in 'MF':
            break
        print('Erro: por favor, digite M para masculino e F para feminino')
    data['idade'] = int(input('Idade: '))
    soma += data['idade']
    lista.append(data.copy())

print(lista)
print('='*100)
# lista com quantidade de pesoas cadastradas.
print(f'Ao todo temos {len(lista)} pessoas cadastradas')

# média de idade
media = soma / len(lista)
print(f'A média de todas as pessoas cadastradas: {media:.2f} anos')

# todas a qtd de pessoas do sexo feminino
print('Mulheres cadastradas do sexo feminino:')
for i in lista:
    if i['sexo'] in 'Ff':
        print(f'{i["nome"]}', end='')
