from math import trunc

#trunc = corta a parte inteira do numero
num = float(input('Digite um número real: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))