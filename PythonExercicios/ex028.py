import random
from time import sleep
nr = random.randint(0, 5)
numero = int(input('Digite o Nr que vc acha q o PC escolheu: '))
print('Processing...')
sleep(1)
if nr == numero:
    print('Venceu')
else:
    print('Perdeu')

print('Nr do PC: {}'.format(nr))

