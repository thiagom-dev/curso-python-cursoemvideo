salario = float(input('Qual e o salario do funcionario? R$'))
if salario <= 1250:
    salarionovo = salario + (salario * 0.15)

else:
    salarionovo = salario + (salario * 0.10)
print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora'.format(salario, salarionovo))