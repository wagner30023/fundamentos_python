def LeiaInt(msg):
        """
       -> Ao fazer a leitura do número a função vai verificar se é um
       :param msg:
       :return: valor

       """
        ok = False
        valor = 0
        while True:
            n = str(input(msg))
            if n.isnumeric():
                valor = int(n)
                ok = True
            else:
                print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            if ok:
                break
        return valor
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar um numero {n} válido.')
print('\n')
help(LeiaInt)
