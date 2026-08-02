n = float(input('Digite o Valor: R$'))
porcentagem = n * 5/100
resultado = n - porcentagem
print ('O produto que custava R${:.2f1p}, na promoção com desconto de 5% vai custar R${:.2f}'.format(n, resultado))
