from datetime import date
ano = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,ano_atual))
if idade == 18:
    print('voce deve se alistar imediatamente!')
    if idade < 18:
     saldo = 18 - idade
    print('Voce não tem 18 anos. ainda faltam {} para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistar ha {} anos!'.format(saldo))