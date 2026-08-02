from time import sleep
distancia = float(input('qual e a distancia da sua viagem '))
print('Processando...')
sleep(0.5)
print('voce esta prestes a começar uma viagem de {:.2f}'.format(distancia),'km')
if distancia <= 200:
    distancia = distancia * 0.50
    print('O preço da sua passagem será de R${:.2f}'.format(distancia))
else:
    distancia = distancia * 0.45
    print('O preço da sua passagem será de R${:.2f}'.format(distancia))
