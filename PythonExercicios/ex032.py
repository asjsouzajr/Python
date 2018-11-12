ano = int(input('Digite o Ano: '))
bissexto = ano % 4
if bissexto == 0:
    print('Ano de {} é um ano Bissexto'.format(ano))
else:
    print('O ano de {} nao é Bissexto'.format(ano))
