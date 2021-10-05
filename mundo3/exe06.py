from time import sleep
from random import randint

def Sorteia():
    print('Sorteando valores.')
    sleep(1)
    for num in range(1, 5):
         sleep(1)
         num = randint(1, 5)
         print(f'{num}',end='')
         if num not in numeros:
             numeros.append(num)

def Soma():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares é: {soma}')

numeros = list()

print('\n')
Sorteia()
print('\n')
print('='*30)
print(f'Lista gerada: {numeros}')
Soma()
