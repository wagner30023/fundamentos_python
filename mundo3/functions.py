def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma(* valores): # * recebe vários valores
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
soma(5,2)
soma(5,9,4)