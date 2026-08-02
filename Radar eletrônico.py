velocidade = float(input('Qual e a velocidade atual do carro '))
if velocidade > 80:
    print('Multado! voce excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('voce deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Muito bem esta conduzindo o veiculo no limite de velocidade')
    print('Tenha um bom dia! dirige com segurança')

