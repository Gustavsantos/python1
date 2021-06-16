
menu = ''
n1 = int(input('Digite o priemiro valor que gostaria de utilizar:  '))
n2 = int(input('Outro numero: '))
while  menu != 5 :
    print ('''[ 1 ] Somar.
[ 2 ] Multiplicar.
[ 3 ] Maior.
[ 4 ] Novos numeros.
[ 5 ] Sair do programa''')
    menu = int(input('Escola uma operação, ou ação! '))
    if menu == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
        print('=-'*15)
    elif menu == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
        print('=-' * 15)
    if menu == 3:
        if n1 > n2:
            print('{} > {}'.format(n1 , n2))
            print('=-' * 15)
        else:
            print('{}  < {}'.format(n1, n2))
            print('=-' * 15)
    if menu == 4:
        n1 = int(input('Quais numeros gostaria de usar agora: '))
        n2 = int(input('Outro numero: '))
        print('=-' * 15)
    if menu > 5:
        print('=-' * 15)
        print('Opcão invalida')
        print('=-' * 15)




