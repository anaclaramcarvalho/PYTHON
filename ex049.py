n = int(input('Digite o número que você deseja ver a tabuada: '))
num = 0
print('TABUADA DO {}' .format(n))
print('-='*6)
for c in range(0,11):
    print('{} X {:2} = {}' .format(n,c,n*c))
