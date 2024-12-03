medida = float(input('Digite a distancia em metros: '))
km = medida / 1000
h = medida / 100
d = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida dada foi {}m, ela convertida \n em quilometros são {}km,\n em hectômetros são {}hm,\n em decâmetros são {}dam,\n em decímetros são {}dm,\n em centímetros são {}cm \n e em milímetros são {}mm' .format(medida,km,h,d,dm,cm,mm))