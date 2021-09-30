mediaIdade = 0
somaIdade = 0
maiorIdadeHomem = 0
nomevelho = ''
totMulherVinte = 0
for p in range(1, 5):
    print('-------------- {} PESSOAS -------------- '.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip()

    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulherVinte += 1
media = somaIdade / 4
print('-----------------------------------------------   -')
print('A Média de idade do grupo é de  {}: '.format(media))
print('O homem mais velho tem {} anos e se chama {}. '.format(maiorIdadeHomem, nomevelho))
print('Quantidade de mulheres com menos de 20 anos = {}: '.format(totMulherVinte))