print('\033[35m-=-\033[m'*20)
print('\033[36mAnalisando Triângulos...\033[m')
print('\033[35m-=-\033[m'*20)

r1 = float(input('Comprimento Reta 1: '))
r2 = float(input('Comprimento Reta 2: '))
r3 = float(input('Comprimento Reta 3: '))


if r1<r2 + r3 and r2<r1 +r3 and r3<r1 +r2:
    print('\033[32mOs segmentos acima PODEM formar triângulo!\033[m')
else:
    print('\033[31mOs segmentos acima NÃO PODEM formar um triângulo.\033[m')