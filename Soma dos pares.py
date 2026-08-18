soma = 0
contador = 0
for c in range(1,7):
    numero = (int(input('Digite um numero: '.format(c))))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Voce informou {} número Pares e a soma foi {}'.format(contador,soma))

