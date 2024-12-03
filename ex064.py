num = cont = soma = 0
num = int(input('Digite um número [999para parar]: '))
while num != 999:
    soma += num
    cont += 1
#print('Você digitou {} números e a soma entre ele foi {}' .format(cont - 1,soma - 999))
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre ele foi {}' .format(cont ,soma))