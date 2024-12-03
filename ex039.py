from datetime import date
atual = date.today().year
ano = int(input('Em que ano vcê nasceu? '))
idade = atual - ano
if(idade < 18):
    tempo = 18 - idade
    print('Você ainda vai se alistar para o serviço militar, faltam {} anos.' .format(tempo))
elif(idade == 18):
    print('Está na hora de se alistar!')
else:
    tempo = idade - 18
    print('Você já deveria ter se alistado, já passou {} anos desde seu periodo de alistamento... resolva essa pendencia.' .format(tempo))

