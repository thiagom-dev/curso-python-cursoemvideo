import math
catetos1 = float(input('Digite o primeiro cateto: '))
cateto2 = float(input('Digite o segundo cateto: '))
resultado = math.sqrt(catetos1 ** 2 + cateto2 ** 2)
print('A hipotenusa vai medir: {:.2f}'.format(resultado))
