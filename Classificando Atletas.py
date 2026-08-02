from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('A categoria do atleta e Mirim.')
    print('O atleta tem {} anos.'.format(idade))
elif idade <= 14:
    print('A categoria do atleta e Infantil.')
    print('O atleta tem {} anos.'.format(idade))
elif idade <= 19:
    print('A categoria do atleta e Junior.')
    print('O atleta tem {} anos.'.format(idade))
elif idade <= 25:
    print('A categoria do atleta e Senior.')
    print('O atleta tem {} anos.'.format(idade))
elif idade > 25:
    print('A categoria do atleta e Master.')
    print('O atleta tem {} anos.'.format(idade))