soma = cont = 0
while True :
    num = int(input('Digite um numero [999 para sair]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores digitados é {soma}')
print(f'A quantidade valores digitados foi {cont}')
