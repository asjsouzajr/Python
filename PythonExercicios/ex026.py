frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()
print('A letra "A", aparece {} vezes na frase'.format(frase.count("A")))
print('A primeira letra "A", apareceu na posicao {}'.format(frase.find('A')))
#outra forma, mas em vez do metódo find usamos agora o index
#print('A letra "A", apareceu primeiro na posicao {}'.format(frase.upper().index('A')))
print('A letra "A" aparece por último na poscicao {}'.format(frase.rfind('A')))


