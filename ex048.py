s = 0
cont = 0
for c in range(1,501,2):
    if c%3==0:
        cont += 1
        s += c
print('O somatorio dos números impares múltiplos por 3 entre 1 e 500 é {}  e nesse intervalo tem {} números' .format(s,cont))