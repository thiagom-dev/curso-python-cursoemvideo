from time import sleep
n1 = int(input('Digite um numero inteiro '))
print('=' *20)
print('1 - Binario')
print('2 - Octal')
print('3 - Hexadecimal')
print('=' *20)
opcao = int(input('Escolha uma opção: '))
print('PROCESSANDO...')
sleep(2)
if opcao == 1:
    bin(n1)
    print('O numero convertido em Binario: {}'.format(bin(n1)[2:]))
elif opcao == 2:
    oct(n1)
    print('O numero convertido em Octal: {}'.format(oct(n1)[2:]))
elif opcao == 3:
    hex(n1)
    print('O numero convertido em Hexadecimal: {}'.format(hex(n1)[2:]))
else:
    print('\033[31mComando Invalido!\033[m')
