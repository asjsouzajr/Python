nome = str(input('Digite seu Nome Completo:')).strip()
print('em Maiusc: {}'.format(nome.upper()))
print('em Minusc.: {}'.format(nome.lower()))
print('Quant Caracteres: {}'.format(nome.__len__() - nome.count(' ')))
#outra forma:
#print('O 1° nome tem {} letras'.format(nome.find(' ')))
separado = nome.split()
print('Primeiro nome tem {} letras e {} caracteres'.format(separado[0],len(separado[0])))

