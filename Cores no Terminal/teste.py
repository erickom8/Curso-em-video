nome = 'Erick'
cores = {'limpa':'\033[m', 
         'azul':'\033[34m', 
         'verde':'\033[32m', 
         'pretoebranco':'\033[7;37m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))