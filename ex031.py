dist = float(input('Qual foi a distância da viagem em km? '))
if dist <= 200:
    valor = dist * 0.5
    print('O valor pago na passagem será {}' .format(valor))
else:
    valor = dist * 0.45
    print('O valor pago na passagem será {}' .format(valor))