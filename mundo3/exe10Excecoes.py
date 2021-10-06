def leiaInt(msg):
    while True:
            try:
                num = int(input(msg))
            except(ValueError, TypeError):
                print('Erro: por favor, digite um número válido não pode ser real ou texto.')
                continue
            except(KeyboardInterrupt):
                print('Entrada de dados interrompida pelo usuário')
                return 0
            else:
                return num
            break
numero = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {numero} ')