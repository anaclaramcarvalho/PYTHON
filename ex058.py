from random import randint
computador = randint(0,10)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Vamos jogar?')
print('Vou pensar em um número entre 0 e 10 e você tenta advinhar qual eu pensei:')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-') 
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos ... Tente mais uma vez.')
print('Você precisou de {} tentativas para me vencer!Parabéns!!!' .format(palpites))