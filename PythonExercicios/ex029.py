veloc = int(input('Digite a Velocidade do Carro: '))
multa = (veloc - 80)*7
if veloc > 80:
    print('Vc foi multado!\nA multa a ser paga é de {}R$'.format(multa))
else:
    print('Obrigado por respeitar o limite de Velocidade')
