import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem COSENO de {:.2f}'.format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(angulo, tangente))
