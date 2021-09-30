from random import choice

n1 = str(input('>> primeiro nome: '))
n2 = str(input('>> segundo nome: '))
n3 = str(input('>> terceiro nome: '))
n4 = str(input('>> quarto  nome: '))

list = [n1,n2,n3,n4]
choice = choice(list)
print('Aluno escolhido: {}'.format(choice))


