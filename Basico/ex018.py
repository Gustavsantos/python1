import random
a1 = input('Digite o nome de um aluno?')
a2 = input('Digite o nome de outro aluno!')
a3 = input('Digite o nome de mais um aluno!')
lista = [a1, a2, a3]
r = random.choice(lista)
print('O vencedor é {}'.format(r))

