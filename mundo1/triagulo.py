import math

# formula => a ao quadrado = b ao quadrado + c ao quadrado

a = float(input('valor de a: '))
# b = float(input('valor de b: '))
# c = float(input('valor de c: '))

result = a ** a
blib = math.sqrt(a)
print('Na mao: {:.2f}'.format(result))
print('utilizando a bibliteca Math: {}'.format(blib))

