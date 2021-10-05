lista = []
aluno = {}

for i in range(1, 4):
    aluno['nome'] = str(input('Digite o nome do aluno: '))
    aluno['media'] = float(input('Média: '))

    if aluno['media'] >= 7:
        aluno['status'] = 'Aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['status'] = 'Recuperação'
    else:
        aluno['status'] = 'Reprovado'
    lista.append(aluno.copy())

print('='*30)
for k,v in aluno.items():
    print(f' - {k} é igual a {v}')

print(' - '*30)
print(lista)
