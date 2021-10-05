lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
pessoa = ('Gustavo', 39, 'M', 99.88)
# del(pessoa)
# Result: NameError: name 'pessoa' is not defined

print(pessoa)
print(sorted(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}')
print('================================')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('================================')

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')



print('Comi pra caramba')