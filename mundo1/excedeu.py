
velocidade = float(input('Qual a velocidade do carro: '))

if velocidade > 80.0:
    multa =(velocidade - 80) * 7
    print('Você excedeu o limite de velocidade de 80KM e deve pagar uma multa de R$ {}'.format(multa))
print('Tenha um bom dia, dirija com segurança!')