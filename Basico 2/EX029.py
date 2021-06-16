v = int(input('Qual a sua velocidade, ao passar pelo radar?'))
m = (v-80)*7
if v>=81:
    print('Você ultrapssou, os limetes, de velocidade!')
    print('O valor total da multa é de R{:.2f}'.format(m))
else:
    print('Voce não foi multado!')