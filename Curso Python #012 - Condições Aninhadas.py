nome = str(input('Qual e o seu nome? '))
if nome == 'Thiago':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome == 'Lucas':
    print('Seu nome e bem popular no brasil!'.format(nome))
else:
    print('Seu nome e bem normal.')
print('Tenha um bom dia, {}!'.format(nome))