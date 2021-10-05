num = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'valores digitados na lista pares {num[0]} e impares {num[1]}')