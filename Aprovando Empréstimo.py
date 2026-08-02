valor_casa = float(input('Valor da Casa: R$'))
salario = float(input('Sálario do comprador: R$'))
ano = int(input('Quantos anos de financiamento:'))
meses = ano * 12
prestacao = valor_casa / meses
limite = (salario * 0.30)
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa, ano, prestacao))
if prestacao > limite:
    print("Emprestimo Negado")
else:
    print("Emprestimo Concedido")
