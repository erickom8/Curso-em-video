import math

a = float(input('Digite o ângulo que deseja: '))

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('O ângulo de {} tem o SENO = {:.2f}'.format (a, s))
print('O ângulo de {} tem o COSSENO = {:.2f}'.format (a, c))
print('O ângulo de {} tem a Tangente = {:.2f}'.format(a, t))
