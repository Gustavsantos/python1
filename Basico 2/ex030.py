n = int(input('Digite um número inteiro, para saber se ele é, par ou impar'))
p = n % 2
print(p)
if p==0:
    print('O número {} é par '.format(n))
else:
   print('O número {} é impár'.format(n))
print('FIM')


