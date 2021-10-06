def Fatorial(n,show=False):
    """
    -> Calcule o Fatoarial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) mostra ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(f'{c} x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f
print(Fatorial(5, show=True))
help(Fatorial)