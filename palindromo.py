frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split() # separa a frase por lista
junto = ''.join(palavras)
inverso = junto[::-1]
print('Vc digitou a frase: {}'.format(junto))
'''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    print('O inverso de {} é {} '.format(junto,inverso))
'''
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')

print(junto, inverso)