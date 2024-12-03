import math
catop = float(input('Digite a medida do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
hi = (catop **2 + catadj**2) **(1/2)
hi2 = math.hypot(catop,catadj)
print('Com os valores dados , o valor da hipotenusa é {:.2f} feito pela equação e {:.2f} pelo import' .format(hi,hi2))