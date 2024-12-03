print('-'*30)
print('Sequência de fibonacci')
print('-'*30)
n = int(input('QUantos termos você quer mostrar? '))
t = 0
t2 = 1
print('^~'*30)
print('{} -> {}' .format(t,t2), end='')
cont = 3
while cont <= n:
    t3 =t + t2
    print('-> {}' .format(t3), end='')
    t =t2
    t2 =t3
    cont += 1
print('FIM!')
print('^~'*30)