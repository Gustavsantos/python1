colocaçao = ('Flamengo' ,'Santos','Palmeiras','Gremio' ,'Athletico-PR','São Paulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia','Vasco ','Atlético-MG','Fluminense','Botafogo','Ceará' ,'Cruzeiro','CSA','Chapecoense' ,'Avaí')
print('-='*11)
print(f'Esta é a colocação dos times:   {colocaçao}')
print('-=' *11)
print(f'5 Primeiros colocados:  {colocaçao[0:5]} ')
print('-=' *11)
print(f'Os 4 ultimos colocados:   {(colocaçao[16:21])}')
print('-='*11)
print(f'Times em ordem alfabetica:  {sorted(colocaçao)}')
print('-='*11)
colo = (colocaçao.index('Chapecoense'))
print(f'O time Chapecoense esta na posição {colo+1}°')