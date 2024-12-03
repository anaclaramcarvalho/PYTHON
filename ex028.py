from random import randint
computador = randint(0,5)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Vamos jogar?')
print('Vou pensar em um número entre 0 e 5 e você tenta advinhar qual eu pensei:')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-') 
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('ganhei!Eu pensei no número {} e não no no {}' .format(computador, jogador))