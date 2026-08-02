n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media >= 7:
    print('Aluno aprovado')
elif 5 <= media < 7:
    print('Aluno em Recuperação')
elif media < 5:
    print('Aluno reprovado')
