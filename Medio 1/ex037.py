nume = int(input('Digite um número para converter'))
print('''Escolha uma opção de conversão
[ 1 ] Conversão binaria
[ 2 ] Coversão octal
[ 3 ] conversãp hexadecimal''')
c = int(input('escola uma opção de conversão'))
if c == 1:
    print('O numero {} convertido para binario é igual {}'.format(nume,bin(nume)[2:]))
elif c == 2:
    print('O numero {} convertido para octal é igual {}'.format(nume,oct(nume)[2:]))
elif c==3:
    print('O numero {} convertido para hexadecimal é igual {}'.format(nume,hex(nume)[2:]))
else:
    print('Você escolheu uma opção invalida ')
