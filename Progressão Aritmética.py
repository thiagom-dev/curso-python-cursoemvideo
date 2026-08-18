print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
num = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('=' * 20)
for c in range(1, 11):
    print(num)
    num = num + razao
print('Acabou...')
print('=' * 20)