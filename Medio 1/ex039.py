from datetime import date
atual = date.today().year
a = int(input('Digite em que ano você nasceu: '))
idade = atual - a
if idade == 18:
    print('Você deve se alistar esse ano')
elif idade > 18:
    print('Você deveria ter se alistado a  {} anos atrás'.format(idade-18))
else:
    print('Ainda faltam, {} para você se alistar'.format(18-idade))