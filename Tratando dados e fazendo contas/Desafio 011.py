l = float(input('Qual a largura da parede (em metros): '))
a = float(input('Qual a altura da parede (em metros): '))
area = l*a

tinta = area/2

print('A área da sua parede é de {}m²\nE ira utilizar {:.3f} Litros de tinta.'.format (area, tinta))