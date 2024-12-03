print('Gerador de PA')
print('-='*10)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão desta PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> ' .format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver a mais? '))
print('Programa finalizado com {} termos mostrados.' ,format(total))
