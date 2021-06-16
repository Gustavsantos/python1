dia = int(input('Quantos dias você alugou o carro?'))
km = float(input('Quantos km você rodou o carro?'))
val = (km * 0.15) + (dia * 60)
print('Você alugou o carro por {} dias e rodou {}km com o carro\nO valor total a ser pago é de R${:.2f}'.format(dia,km,val))