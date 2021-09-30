valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: R$ '))
prestacao = valor_casa / (anos * 12)
minimo = (salario * 30)/100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, anos), end='')
print(' A prestação mensal será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo concedido')
else:
    print('Emprestimo negado')
