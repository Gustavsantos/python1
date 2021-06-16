import random
print('Vamos separar a ordem de apresentação ')
a1 = input('Digite um nome')
a2 = input('O segundo nome')
a3 = input('O teiceiro nome ')
a4 = input('O quarto nome')
lista = [a1,a2,a3,a4]
r = random.shuffle(lista)
print('A ordem deve ser')
print(lista)
