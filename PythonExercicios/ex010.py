real = float(input('Quantos Reais vc tem na carteira ? R$'))
dolar = 1/3.27
convert = real * dolar
print('{} reais convertidos em dolar dá US${:.2f}'.format(real,convert))