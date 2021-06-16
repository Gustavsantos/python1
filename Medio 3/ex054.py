from datetime import date
atual = date.today().year
cont = 0
soma = 0
for ano in range (1,7):
    nasc = int(input('Em qual ano você nasceu?  '))
    idade = atual - nasc
    if idade >= 18:
        cont +=1
    elif idade <= 17:
        soma +=1
print('Entre todas as pessoas {} são maiores de idade!'.format(cont))
print('Entre todas as pessoas {} são menores de idade!'.format(soma))
