import math

c1 = float(input('Comprimento de um cateto: '))
c2 = float(input('Comprimento do outro cateto: '))

hip = math.hypot (c1, c2)
print('A hipotenusa tem valor de: {:.2f}'.format (hip))