data = dict()
partidas = []
data['nome'] = str(input('Digite o nome: '))
qtd_partidas = int(input(f'Quantas partidas {data["nome"]} jogou ?  '))

for i in range(0, qtd_partidas):
    partidas.append(int(input(f'Quantos gols na partida {i}: ')))

''' data['gols'] recebe um cópia de partidas  partidas[:]'''

data['gols'] = partidas[:]
data['total'] = sum(partidas)
# print(data)
print('='*50)
print(f'Nome do jogador: {data["nome"]}')
print(f'Quantidade de partidas: {qtd_partidas}')
print(f'Quantidade total de gols marcados: {sum(data["gols"])}')
for c, v in enumerate(data['gols']):
    print(f'Na {c} partida marcou {v} gol(s).')


