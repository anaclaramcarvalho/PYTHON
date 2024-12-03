listagem = ('Lápis', 1.75,
            'Borracha',2,
            'Caderno',10.90,
            'Estojo',25,
            'Transferidor',4.20,
            'Compasso',9.99,
            'Mochila',100,
            'Canetas',16.50,
            'Livro',30.70)
print('-'*37)
print(f'{"LISTAGEM DE PRODUTOS E SEUS PREÇOS":^37}')
print('-'*37)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end ='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*41)