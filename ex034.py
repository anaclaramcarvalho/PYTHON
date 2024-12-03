salário = float(input('Qual é o salario do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 0.15)
else:
    novo = salário + (salário * 0.10)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.' .format(salário, novo))