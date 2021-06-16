n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2
if  media >= 7:
   print('Parabéns sua media foi de {} você  \033[32mAPROVADO\033[m!'.format(media))
elif media < 5 :
    print('Sua media {} você foi \033[31mREPROVADO\033[m!'.format(media))
    print('Estude mais')
elif media < 7:
    print('Sua media {} voce esta de recuperação'.format(media))