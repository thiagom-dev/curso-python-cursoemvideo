dias = float(input('Quantos dias alugados? '))
kilo = float(input('Quantos Kilometros rodados? '))
diavalor = dias * 60
kilovalor = kilo * 0.15
total = diavalor + kilovalor
print('O total de dias alugados foi R${:.2f} e de kilometragem R${:.2f}'.format( diavalor , kilovalor))
print('O total a Pagar R${:.2f}'.format(total))

