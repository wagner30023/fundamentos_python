
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Você esta abaixo do peso, o seu IMCé: {:.1f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Você esta com o peso ideal, o seu IMC é: {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('Você esta com sobrepeso, o seu IMCé: {:.1f}'.format(imc))
elif imc >= 40:
    print('Você esta com obesidade CUIDADO!, o seu IMC é: {:.1f}'.format(imc))
