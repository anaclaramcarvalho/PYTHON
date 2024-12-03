from time import sleep
n = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('---------------------------')
    print('         MENU')
    print('---------------------------')
    print('[1] SOMA')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    opção = int(input('Qual opçaõ você escolheu? '))
    if opção == 1:
        r = n + n2  
        print('A soma entre {} e {} é {}.' .format(n,n2,r))    
    elif opção == 2:
        r = n * n2 
        print('A multiplicação entre {} e {} é {}.' .format(n,n2,r))      
    elif opção == 3:
        if n > n2:
            r = n 
            print('O maior número digitado foi {}.' .format(r))         
        elif n == n2:
            r = n2 
            print('O maior número digitado foi {}.' .format(r))       
        else:
            r = n2   
            print('O maior número digitado foi {}.' .format(r))  
    elif opção == 4:
        print('Informe os novos números: ')
        n = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.Tente novamente.')
        sleep(3)
print('Você saiu do programa!')

        

            