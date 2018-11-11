dias = int(input('Quantos dias o carro foi alugado ? '))
km = float(input('Quantos Km foram rodados ? '))
precoDia = dias * 60
precoKm = km * 0.15
precoTotal = precoDia + precoKm
print('O carro foi alugado por {} dias e rodou {} kilometros \n O Total a pagar será de R${:.2f}'.format(dias, km,precoTotal))
