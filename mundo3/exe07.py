def Soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = Soma(1, 2)
r2 = Soma(1, 5, 9 )
r3 = Soma(1, 2, 5)
print(f'A soma dos valores são: {r1,r2,r3}')

def Fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = Fatorial(5)
f2 = Fatorial(4)
f3 = Fatorial()

print(f'Os resultados são {f1}, {f2}, {f3}')