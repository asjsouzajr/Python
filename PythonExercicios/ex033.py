nr1 = float(input('Digite um primeiro Número: '))
nr2 = float(input('Digite um segundo Número: '))
nr3 = float(input('Digite um terceiro Número: '))
if nr1 > nr2 and nr1 > nr3:
    print('O Primeiro Nr digitado ({}) é o maior dos 3 digitados'.format(nr1))
if nr2 > nr3 and nr2 > nr1:
    print('O Segundo Nr digitado ({}) é o maior dos 3 digitados'.format(nr2))
if nr3 > nr1 and nr3 > nr2:
    print('O Terceiro Nr digitado ({}) é o maior deles'.format(nr3))
