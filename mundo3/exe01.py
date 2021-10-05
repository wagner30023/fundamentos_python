estado = dict()
brasil = list()

for i in range(1, 3):
    estado['uf'] = str(input('Unidade federativa: ')).upper()
    estado['sigla'] = str(input('Sigla do estado: ')).upper()
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()