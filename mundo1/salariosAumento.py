
salario = float(input('Digite o seu salario: '))

if salario <= 1250:
    reajuste = salario + (salario * 15 / 100)
else:
     reajuste = salario + (salario * 10 / 100)


print('===================================')
print('Salario: {}'.format(salario))
print('Reajuste: {}'.format(reajuste))