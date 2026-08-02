import random
from time import sleep
print('-=-' * 30)
print('Vou pensar em um número inteiro entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)
computador = random.randint(0, 5)
numero = int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if numero == computador:
    print('Você acertou!')
else:
    print('Você errou!')
    print('Eu pensei no número', computador)


