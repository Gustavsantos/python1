n1 = int(input('Digite um numero para saber qual é o maior: '))
n2 = int(input('Digite outro  valor: '))
if n1 > n2:
    print('{} É maior que {}'.format(n1,n2))
elif n2 > n1:
    print('{} É maior que {}'.format(n2,n1))
else:
    print(' {} É igual a {}'.format(n1,n2))
