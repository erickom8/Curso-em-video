salário = float(input('Qual o salário de um funcionário? '))

if salário<= 1250:
    print('Quem ganhava R${} passa a ganhar: R${}'.format(salário, salário*1.15))
else:
    print('Quem ganhava R${} passa a ganhar: R${}'.format(salário, salário*1.1))
