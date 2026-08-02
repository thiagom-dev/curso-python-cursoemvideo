print('=' * 11, 'Loja Desconhecida', '=' * 11)
preco = float(input('Preço das Compras: R$'))
print('Qual e a formas de pagamento?')
print('[1] À vista dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    desconto = preco * 0.10
    novo_preco = preco - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. teve um desconto de 10%'.format(preco, novo_preco))
elif opcao == 2:
    desconto = preco * 0.05
    novo_preco = preco - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. teve um desconto de 5%'.format(preco, novo_preco))
elif opcao == 3:
    print('Sua compra foi de R${:.2f}'.format(preco))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    novo_preco = preco + (preco * 0.20)
    valor_parcela = novo_preco / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parcelas, valor_parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, novo_preco))
print('Obrigado pela pagamento!')
print('=' * 41)