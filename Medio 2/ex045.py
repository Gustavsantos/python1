import random
from time import sleep
print('''Vamos jogar JOKENPÔ
Escolha:
[ 0 ] Pedra.
[ 1 ] Papel.
[ 2 ] Tésoura.''')
jogador = int(input('Escolha uma ação!'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
açoes = 'pedra','papel','tésoura'
computador = random.randint (0,2)
print('-='*15)
print('O computador escolheu,{}.'.format (açoes[computador]))
print('O jogador escolheu {}'.format(açoes[jogador]))
print('-='*15)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Parabéns você venceu!')
    elif jogador == 2:
        print('Você perdeu!')
    else:
        print('Jogada invalida!')
if computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('Você perdeu!')
    elif jogador == 2:
        print('Parabéns, você venceu!')
    else:
        print('Opção invalida!')
if computador == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('Parabéns você venceu!')
    elif jogador == 1:
        print('Você perdeu')
    else:
        print('Opção invalida!')

