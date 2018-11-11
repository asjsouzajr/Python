cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:6].upper()== 'SANTO')

'''
resultado = cidade.upper().find('SANTO')
if resultado != -1:
    print('A cidade {}, comeca com a palavra Santo'.format(cidade))
else:
    print('A cidade {}, nao comeca com a palavra Santo'.format(cidade))
'''
