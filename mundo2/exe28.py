valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break

print(f' você digitou a quantidade de {len(valores)} elementos. ')
valores.sort(reverse=True)
print(f' os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f' o valor {5} está dentro da lista')
else:
    print('A lista não contém o valor 5.')