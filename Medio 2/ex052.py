tot = 0
n1 = int(input('Qual o numero, que deseja saber se é primo? '))
for c in range(1, n1 +1):
    if n1 % c == 0:
        print('\033[33m', end=' ')
        print(c, end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
        print(c, end=' ')
if tot == 2:
    print('\n\033[mO número {} é primo, e foi divido {} vezes.'. format(n1,tot))
else:
    print('\n\033[mO numero {} foi dividido {} vezes e por isso não é primo.'.format(n1,tot))