n = int(input('Digite ume numero de 0 a 9999:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('O numero {} tem.\nUnidades: {}\nDezenas: {}\nCentenas: {}\nMilhar: {}'.format(n,u,d,c,m))