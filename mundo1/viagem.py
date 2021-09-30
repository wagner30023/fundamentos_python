distancia = float(input('Qual é a distância de sua viagem: '))
print('você esta prestes a começar uma viagem de 0 km')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Eo preço da sua viagem será de R${:.2f}'.format(preco))