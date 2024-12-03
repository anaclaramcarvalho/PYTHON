ano = int(input('Digite o ano do seu nascimento: '))
idade = 2023 - ano
if(idade <= 9):
    print('Você está na categoria MIRIM!')
elif( 9 < idade <= 14):
    print('Você está na categoria INFANTIL!')
elif(14 < idade <= 19):
    print('Você está na categoria JUNIOR!')
elif(19 < idade <= 25):
    print('Você está na categoria SÊNIOR!')
else:
    print('Você está na categoria MASTER!')