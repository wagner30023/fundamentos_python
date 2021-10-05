valores = []
# enumerate pega o valor dachave quanto o do valor

for i in range(1, 21):
    valores.append(i)
print(valores)

for c,v in enumerate(valores):
    print(f'{v}..', end='')