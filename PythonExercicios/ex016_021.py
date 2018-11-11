'''     Ex 16
import math
num = float(input('Digite um Nr:'))
print('O Nr {} tem a parte inteira {}'.format(num,math.floor(num)))'''
'''     Ex 17
from math import sqrt
print("Insira os Catetos do triangulo:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("A Hipotenusa é", c)'''
'''     Ex 19
import random
al1 = input('Digite o nome de um Aluno:')
al2 = input('Digite o nome de um segundo Aluno:')
al3 = input('Digite o nome de um terceiro Aluno:')
r = [al1,al2,al3]
print('O Aluno {} é o escolhido para apagar o quadro'.format(random.choice(r)))'''
'''     Ex 20
import random
print('Digite os Nomes dos Alunos')
al1 = input('Digite Aluno 1:')
al2 = input('Digite Aluno 2:')
al3 = input('Digite Aluno 3:')
list = [al1,al2,al3]
ordem = random.sample(list,k=3)
print('A ordem de Apresentacao será {}'.format(ordem))'''
'''Ex 21
import playsound
playsound.playsound('ex021.mp3')'''



