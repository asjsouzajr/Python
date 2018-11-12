r1 = int(input('Digite o comprimento do primeiro lado: '))
r2 = int(input('Digite o comprimento do segundo lado: '))
r3 = int(input('Digite o comprimento do terceiro lado: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O triangulo é possível')
else:
    print('Nao dá pra formar o triangulo')
