totalmaior18 = totaldehomens = totaldemulheresmenores20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        totalmaior18 += 1
    if sexo == 'M':
        totaldehomens += 1
    if sexo == 'F' and idade < 20:
        totaldemulheresmenores20 +=1

    resposta = ' '
    while resposta not in 'SN': 
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {totalmaior18}')
print(f'Temos {totaldehomens} homens cadastrados.')
print(f'Temos { totaldemulheresmenores20} de mulheres cadastradas com menos de 20 anos.')