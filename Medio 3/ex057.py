mascu = 'M'
femi = 'F'
r = ''
while r != femi and r != mascu :
    r = str(input('Qual é seu sexo? [M/F] ')).upper()
    if r != femi and r != mascu:
        print('Opção invalida Digite novamente! ')
print('Você escolheu a opção {}.'.format(r))

