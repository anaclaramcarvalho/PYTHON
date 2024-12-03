print('='*30)
print('{:^30}'.format('BANCO ANX'))
valor = int(input('Que valor voce quer sacar? R$'))
total = valor
cédulas = 50
totalcédulas = 0
while True:
    if total >= cédulas:
        total -= cédulas
        totalcédulas += 1
    else:
        if totalcédulas > 0:
            print(f'Total de {totalcédulas} cédulas de R${cédulas}')
        if cédulas == 50:
            cédulas = 20
        elif cédulas == 20:
            cédulas = 10
        elif cédulas == 10:
            cédulas = 1
        totalcédulas = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO ANX!Tenha um bom dia! :)')