''' TEORIA
tempo = int(input('Quantos anos tem seu carro? '))
Modo Normal:
    if tempo <= 3:
    print('Seu carro está bem novinho')
else:
    print('Seu carro já nao é tao novo')
#Modo Simplificado:
print('Carro novo'if tempo <=3 else'Carro velho')'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if media >= 7:
    print('Aluno Aprovado com Média {:.2f}'.format(media))
else:
    print('Aluno reprovado com Média {:.2f}'.format(media))
