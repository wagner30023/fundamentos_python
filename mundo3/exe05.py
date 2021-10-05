def Area():
    print('='*30)
    print('Controle de terrenos')
    print('=' * 30)
    b = float(input('Largura (m): '))
    h = float(input('Comprimento (m): '))
    a = b * h
    print(f'O calculo da área é de: {a:.2f}')
Area()