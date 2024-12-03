while True:
    n = int(input('Qual valor voce deseja saber a tabuada? '))
    print('_ '*30)
    if n < 0:
         break
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print('_'*30)
print('PROGRAMA ENCERRADO!')
print('Volte sempre.')