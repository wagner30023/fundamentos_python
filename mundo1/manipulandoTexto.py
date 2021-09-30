

frase = 'curso em video Python'

print(len(frase))
print(frase[3:13])
print(frase.replace('Python', 'Android'))
print(frase.capitalize())
print(frase.title())

print(' - '.join(frase))
print(frase.title())
# print(frase.find('video'))
# lista = list(frase)
# print(lista)
# print(frase.split())

cars = ['audi', 'bmw', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
