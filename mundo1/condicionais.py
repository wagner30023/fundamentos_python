
tempo = int(input('Quanto anos vc tem: '))

if tempo:
    print('Anos: {}'.format(tempo))
elif not tempo:
    print('utilize apenas numeros inteiros')
else:
    print('Numero incorreto')