from random import shuffle

 # sorteado uma ordem de lista

aluno1 = str(input('>> Primeiro aluno: '))
aluno2 = str(input('>> Segundo aluno:  '))
aluno3 = str(input('>> Terceiro aluno: '))
aluno4 = str(input('>> Quarto aluno: '))

list = [aluno1, aluno2, aluno3, aluno4]
shuffle(list)

print('O primeiro aluno que irá apresenta é: {}'.format(list))