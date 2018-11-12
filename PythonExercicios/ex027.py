nome = str(input('Digite seu nome: ')).strip()
print('Muito prazer em te conhecer!')
nome = nome.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
#ou simplesmente assim:
#print('Seu último nome é {}'.format(nome[-1]))


