print('Digite tres valores para saber qual, é o menor e o maior')
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    maior = a
if c>b and c>b:
    maior = c
if b>a and b>c:
    maior = b
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = a
if c<a and c<b:
    menor = c
print( 'O maior némero é {}'.format(maior))
print('O menor número é {}'.format(menor))

