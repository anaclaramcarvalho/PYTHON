n = float(input('Digite um número: '))
d = n*2
t = n*3
rq = n**(1/2)
print('O número digitado foi {}, o seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}' .format(n,d,t,rq))
print('O número digitado foi {}, o seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}' .format(n,(n*2),(n*3),pow(n,(1/2))))