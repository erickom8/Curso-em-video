numero = float(input('\033[35m Me diga um número qualquer: \033[m'))

if (numero%2) == 0:
    print( 'O número {} é par'.format(numero))
else: 
    print('O número {} é impar'.format(numero))