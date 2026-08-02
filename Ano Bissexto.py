from datetime import datetime, date
ano = int(input('que ano quer analisar? coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} e BISSEXTO'.format(ano))
else:
    print('o ano {} não e BISSEXTO'.format(ano))

