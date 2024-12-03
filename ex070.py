total = tprodutosmaismil = maisbarato = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        tprodutosmaismil += 1
    if cont == 1:
        maisbarato = preço
        barato = produto
    else:
        if preço < maisbarato:
            maisbarato = preço
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('CONTA'))
print(f'O total da compra foi de R${total: .2f}')
print(f'Temos {tprodutosmaismil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} ,ele custa R${maisbarato:.2f}')