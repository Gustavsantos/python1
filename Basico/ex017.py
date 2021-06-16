from math import radians,tan,sin,cos
an = float(input('Digite o valor do angulo:'))
se= sin(radians(an))
print('O seno do ângulo é {:.2f} '.format(se))
ta = tan(radians(an))
print('A tangente do ângulo é {:.2f}'.format(ta))
co = cos(radians(an))
print('O coseno do ângulo é {:.2f}'.format(co))