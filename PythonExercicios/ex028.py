import random

nr = (random.randint(0, 5))
numero = str(input('Digite o Nr que vc acha q o PC escoolheu: '))
if nr == numero:
    print('Venceu')
else:
    print('Perdeu')

print(nr)

