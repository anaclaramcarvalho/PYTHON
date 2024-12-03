num = int(input('Digite qual número você gostaria de fazer conversão de base: '))
print('=-'*20)
print('''DIGITE:
[1]Mudar para a base binária
[2]Mudar para octagonal
[3]Mudar para hexadecimal''')
resp =int(input('A opção escolhida foi:'))
print('=-'*20)
if resp == 1:
    print('O número {} em base binária fica {}' .format(num,bin(num)[2:]))
elif resp == 2:
    print('O número {} em base octagonal fica {}' .format(num,oct(num)[2:]))
elif resp == 3:
    print('O número {} em base hexadecimal fica {}' .format(num,hex(num)[2:]))
else:
    print('Opção invalida!Tente novamente.')