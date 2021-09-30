num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão 
[1] converter para binário
[2] converter para Octal
[3] converter para Hexadecimal ''', end='')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) # [2:] fatiamneto de strings
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. ')