from datetime import date
a = int(input('Digite um ano, para analisarmos se é bisexto ou 0 para saber o ano atual'))
if a==0 :
    a=date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é bisexto '.format(a))
else:
    print('O ano {} não é bisexto'.format(a))

