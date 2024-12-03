vcasa = float(input('QUal é o valor da casa que pretende comprar? R$'))
salario = float(input('Qual é o seu salário? '))
anos = float(input('Em quantos anos você pretende pagar a casa? '))
meses = anos * 12
prestmensal = vcasa / meses
if (0,3*salario <= prestmensal):
    print('Empréstimo negado')
else:
    print('Empréstimo aceito!Boa compra')