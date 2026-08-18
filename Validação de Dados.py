sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Dados inválidos. Por favor, ', end='')
    sexo = str(input('informe seu sexo [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')