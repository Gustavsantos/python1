from random import choice
n1 = int(input('Digite um  numero'))
n2 = int(input('Digite outro numero'))
n3 = int(input('Mais um numero'))
lista = [n1,n2,n3]
r = choice(lista)
print ('O vencendor é o nuemero  {}'.format(r))
