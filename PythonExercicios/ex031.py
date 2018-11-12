dist = float(input('Informe a distância da Viagem em KM: '))
if dist > 200:
    passagem = dist * 0.45
    print('O valor da passagem será de {}R$'.format(passagem))
else:
    passagem = dist * 0.50
    print('O valor da passagem será de {}R$'.format(passagem))
