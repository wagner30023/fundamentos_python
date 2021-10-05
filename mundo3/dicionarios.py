pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

print(pessoas['nome'])
print(pessoas['idade'])

# print(f' O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# adicionando pessoas no dicionario
pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f' {k} = {v}')

