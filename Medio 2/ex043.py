peso = float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua altura? (M) '))
imc = peso / (altura * altura)
print('Seu imc é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você esta abaixo do peso!')
elif imc <= 25:
     print('Seu peso é ideal!')
elif imc <= 30:
    print('Você esta com sobrepeso!')
elif imc <= 40:
    print('Você esta com obesidade, CUIDADO!!')
else:
    print('Voce esta com obesidade mórbida, CUIDADO!!')
