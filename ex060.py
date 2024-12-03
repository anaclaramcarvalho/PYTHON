num = int(input('Digite o número que deseja saber o fatorial: '))
fat = 1
i = 2
while i <= num:
    fat = fat*i
    i += 1
print('O fatorial do número digitado é {}.' .format(fat))

#from math import factorial
#n = int(input('Digite um número que deseja saber o fatorial:' ))
#f = factorial(n)
#print('O fatorial de {}.' .format(n,f))

 #n = int(input('Digite um número que deseja saber o fatorial: ')
 #c = n
 #f = 1
 #print('Calculando {}! = ' .format(n), end='')
 #while c > 0
 #print('{}' .format(c), end='')
 #print('x' if c > 1 else ' = ', end='')
 #f *= c
 #c -= 1
 #print('{}', .format(f)) 