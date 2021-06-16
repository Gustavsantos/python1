primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
r = primeiro
c = 1
while c <= 10:
    c += 1
    print('{}'.format(r), end=  ' -> ')
    r += razao
print('Fim')



