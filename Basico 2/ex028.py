import random
print(' ola!')
print('Quero te desafiar, sera que voce consegue, adivinhar em qual numero estou pensando?')
R = random.randint(0,5)
n = int(input('Vamos la,Digite um nemero de 0 a 5, em qual numero estou pensando?'))
if n==R:
    print('PARABÉNS você acertou')
else:
    print('Você perdeu ')
print('EU estava pensando no numero {}'.format(R))
