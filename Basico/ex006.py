n1 = int(input('Digite sua primeira nota:'))
n2 = int(input('Digite sua segunda nota'))
n = (n1 + n2) /2
if n < 5:
    print('Sua note é menor que a media, você foi \033[1;31mREPROVADO\033[M')
else:
    print('Parabéns você foi \033[1;32mAPROVADO\033[m')
