frase = str(input('Digite uma palavra para saber, se ela é um políndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if junto == inverso:
    print('A palavra {} é um políndromo '.format(frase))
    print(inverso)
else:
    print('A palavra {} não é uma políndromo'.format(frase))
    print(inverso)
