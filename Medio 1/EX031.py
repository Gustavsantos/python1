km = int(input('Quantos kms tem sua viagem?'))
v = km * 0.45
v2 = km * 0.50
if km>=200:
    print('O valor a pagar por km sera R$0.45 e o total a pagar é R${:.2f}'.format(v))
else:
    print('O valora pagar por km sera R$0.50 e o total a pagar é R${:.2f}'.format(v2))
