'''from math import sqrt
co = float(input('Digite o valor do cateto oposto'))
ad = float(input('Digite o valor do cateto adjacente:'))
hp = sqrt( co ** 2 + ad ** 2)
print('O valor da hiponenusa é: {:.2f} '.format(hp))'''

from math import hypot
co = float(input('Digite o valor do cateto oposto'))
ad = float(input('Digite o valor do cateto adjacente'))
hi = hypot(co,ad)
print('o valor da hipotenusa é {:.2f}'.format(hi))
