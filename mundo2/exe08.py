r1 = float(input('segmento 1: '))
r2 = float(input('segmento 2: '))
r3 = float(input('segmento 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos forma um triângulo ',end='')
    if r1 == r2 and r2 == r3:
        print('>> Equilatero!')
    elif r1 != r2 != r3 != r1:
        print('>> Escaleno')
    else:
        print('>> Isôsceles')
else:
    print('Os segmentos Não forma um triângulo')

# condição aninhada