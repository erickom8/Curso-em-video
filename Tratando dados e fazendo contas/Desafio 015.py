km = float(input('Quantos km o carro percorreu? '))
d = float(input('Quantos dias alugados? '))

pkm = 0.15*km
pd = 60*d
print('O preço total será de R${}'.format(pkm+pd))