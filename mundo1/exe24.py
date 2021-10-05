num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
print(num)
print(sorted(num))
num.insert(2,0)
if 5 in num:
    num.remove(5)
else:
    print('Não existe')
print(num)
num.pop(3)
print(num)
print(f'Essa lista tem {len(num)} elementos.')