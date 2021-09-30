nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno e {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('REPROVADO ')
elif (media >= 5) and (media <= 6.9):
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')