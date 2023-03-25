viagem = float(input('Qual será a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(viagem))

if viagem <=200:
    print('E o preço da sua passagem será de R${:.2f}'.format(viagem/2))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(viagem*0.45))