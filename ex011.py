l = float(input('Digite a largura da parede que se deseja pintar: '))
a = float(input('Digite a altura da parede que se deseja pintar: '))
area = l * a
tinta = area / 2
print('Sua parede tem {}metros quadrados e será necessario {}l de tinta para pinta-lá' .format(area, tinta))