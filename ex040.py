nota1 = float(input('Digite a primeira nota: '))
nota2 =float(input('Digite a segunta nota: '))
media =(nota1 + nota2) / 2
if(media < 5):
    print('REPROVADO!')
elif(5 < media < 6.9):
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!APROVEITE AS FERIAS.')