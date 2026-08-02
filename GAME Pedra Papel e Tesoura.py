from random import choice
from time import sleep

opcoes = ['Pedra', 'Papel', 'Tesoura']

computador = choice(opcoes)

print('-=' * 15)
print('VAMOS JOGAR JOKENPÔ!')
print('-=' * 15)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)

if jogador == 0:
    escolha_jogador = 'Pedra'
elif jogador == 1:
    escolha_jogador = 'Papel'
elif jogador == 2:
    escolha_jogador = 'Tesoura'
else:
    escolha_jogador = 'Inválido'

print('-=' * 15)
print(f'Computador jogou {computador}')
print(f'Jogador jogou {escolha_jogador}')
print('-=' * 15)

if escolha_jogador == 'Inválido':
    print('Jogada inválida!')
elif computador == escolha_jogador:
    print('EMPATE!')
elif (computador == 'Pedra' and escolha_jogador == 'Tesoura') or \
     (computador == 'Papel' and escolha_jogador == 'Pedra') or \
     (computador == 'Tesoura' and escolha_jogador == 'Papel'):
    print('COMPUTADOR VENCEU!')
else:
    print('JOGADOR VENCEU!')