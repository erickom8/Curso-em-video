nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculas é {}'.format (nome.upper()))
print('Seu nome em minúsculas é {}'.format (nome.lower()))
print('Seu nome em têm ao todo {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome possui {} letras.'.format(nome.find (' ')))
separa = nome.split()
print('Seu primeiro nome possui {} letras.'.format(len(separa[0])))
