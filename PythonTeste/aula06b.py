#n1 = int(input('Digite um nr: '))
#n2 = int(input('Digite outro nr: '))
#soma = n1+n2
#print('A soma de {} e {} é: {}'.format(n1, n2, soma))

algo = input('Digite algo: ')
print('É alfanumerico: ',algo.isalnum())
print('É numerico: ',algo.isnumeric())
print('Está em maiúsculo: ',algo.isupper())
print('Está em minúculo: ',algo.islower())
print('Qual o tipo: ',(type(algo)))
