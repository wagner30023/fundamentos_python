valores = []

for i in range(0, 6):
    num = int(input('digite um numero: '))
    valores.append(num)
print(valores)
print(f'Maior valor da lista {max(valores)}')
print(f'Menor valor da lista {min(valores)}')

for c, v in enumerate(valores):
    print(f' na posição   {c}', end='')
    print(f' na posição {v}', end='')