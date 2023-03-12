m = int(input('Digite o tamanho em metros:'))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print('O tamanho em quilômetros é {}km\nO valor em hectômetro é de {}hm.'.format (km, hm))
print('O tamanho em decâmetros é {}dam'.format (dam))
print('O tamanho em decímetros é {}'.format (dm))
print('O tamanho ém centímetros é {}'.format (cm))
print('O tamanho ém milímetros é {}'.format (mm))