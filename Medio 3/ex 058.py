from random import randint
import time
print('Vamos jogar!!')
print('Vou pensar em um numero, tente acertar!')
print('...')
time.sleep(1)
escolha = 1
conteescolhas = 0
computador = randint(1,10)
while escolha != computador:
    escolha = int(input('Escolha um numero de 1 a 10! '))
    if escolha == computador:
        conteescolhas +=1
        print('=-='*15)
        print('Eu escolhi o numero {}'.format(computador))
        print('Parabéns você venceu e usou {} tentativas!.'.format(conteescolhas))
        print('=-='*15)
    else:
        conteescolhas += 1
        print('Tente novamente')




