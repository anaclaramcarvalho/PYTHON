import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem SENO de {:.2f}' . format(ang,seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo de {} tem COSSENO de {:.2f}' . format(ang,cosseno))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(ang,tang))
