from datetime import date
nas = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - nas

if idade <= 9:
    print('O atleta tem, {} anos!'.format(idade))
    print('E pertense a categoria MIRIN!')
elif idade <= 14:
    print('O atlesta tem, {} anos!'.format(idade))
    print('E pertense a categoria INFANTIL!')
elif idade <= 19:
        print('O atleta tem, {} anos'.format(idade))
        print('E pertense a categoria JUNIOR!')
elif idade <= 25:
    print('O atleta tem, {} anos!'.format(idade))
    print('E pertense a categoria SENIOR!')
else:
    print('O atleta tem, {} anos!')
    print('E pertense a categoria MASTER!'.format(idade))

