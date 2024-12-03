km = float(input('Digite a quantidade de quilometros percorrido pelo carro alugado: '))
d = int(input('Digite para quantos dias o carro foi alugado: '))
vt = (d * 60) + (km * 0.15)
print('O carro foi alugado por {} dias e percorreu {}km, totalizando R${}' .format(d,km,vt))