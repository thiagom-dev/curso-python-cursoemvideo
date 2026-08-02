print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
if reta1 >= reta2 + reta3 or reta2 >= reta1 + reta3 or reta3 >= reta1 + reta2:
    print('Os seguimentos acima não pode formar um triângulo')
else:
    print('Os seguimentos acima pode formar um triângulo')
    if reta1 == reta2 and reta2 == reta3:
        print('O triangulo e Equilatero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('O triangulo e Isoceles')
    else:
        print('O triangulo e Escaleno')