frase = input('Digite uma frase: ')
frase = frase.lower().replace(' ', '')
inversa = ''
for i in range(len(frase) - 1, -1, -1):
    inversa += frase[i]
print('A frase Inversa: {}'.format(inversa))
if frase == inversa:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
