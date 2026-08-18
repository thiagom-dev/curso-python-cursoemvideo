num = int(input('Digite um numero: '))
tot = 0
for c in range(1,num + 1):
    if num % c == 0:
        print('\033[34m')
        tot += 1
    else:
        print('\033[31m')
    print('{}'.format(c) ,end=' ')
print('o numero {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print('o numero {} foi primo'.format(num))
else:
    print('O numero {} não e primo'.format(num))
