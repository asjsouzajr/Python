sal = float(input('Digite o Salário do Funcionario: '))
if sal > 1250:
    novoSal = sal * 1.10
    print('O novo Salário com aumento será de {:.2f}R$'.format(novoSal))
else:
    novoSal = sal * 1.15
    print('O novo Salário será de {:.2f}R$'.format(novoSal))
