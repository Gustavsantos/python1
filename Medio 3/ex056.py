total = 0
media = 0
hmais = 0
no = ''
contm = 0
from datetime import date
atual = date.today().year

for p in range(1,5):
    print('{}° Pessoa'.format(p))
    nome = str(input('Nome: ')).strip().capitalize()
    ns = int(input('O ano em que nasceu: '))
    sexo = str(input('Sexo: ')).strip().upper()
    idade = atual - ns
    total += idade
    media = total/4
    if p == 1 and sexo == 'M':
        hmais = idade
        no = nome
    if idade > hmais and sexo == 'M':
        hmais = idade
        no = nome
    if idade < 20 and sexo == 'F':
        contm += 1
print('Existem, {} mulheres com  menos de 20 anos'.format(contm))
print('O homem mais, velho tem {} e se chama {}'.format(hmais, no))
print('A media de idade, é de {} anos'.format(media))
