times = ('Athletico','Bahia','Botafogo','Atlético','Bragantino','Palmeiras','Flamengo','São Paulo','Internacional','Cruzeiro','Grêmio','Fortaleza','Criciúma','Corinthians','Juventude','Fluminense','Vasco d Gama','Vitória','Atlético-GO','cuiabá')
print('-='*15)
print(f'TIMES DO BRASILEIRÃO')
for t in times:
    print(t)
print('-='*15)
print(f'Os 5 primeiros times colocados são : {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'O Atlético  está na {times.index("Atlético")+1} posição')