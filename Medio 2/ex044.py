vl = float(input('Qual o valor da sua compra? '))
print('''Qual sera a forma de pagamento?
[ 1 ] A vista no dinheiro com 10% de descosto.
[ 2 ] A vista no cartão de credito com 5% de desconto.
[ 3 ] Em ate 2x sem desconto.
[ 4 ] 3x ou mais  com juros de 20%''')
forma = int(input('Qual a forma de pegamento? '))
if forma == 1:
    print('Você tem 10% de desconto o valor a ser pago com desconto é R${:.2f}.'.format(vl-(vl * 10 / 100)))
elif forma == 2 :
    print('A vista no cartão de credito  R${:.2f}.'.format(vl-(vl * 5 / 100)))
elif forma == 3:
    print('Parcelado em 2x  sem desconto o valor é de R${:.2f}.'.format(vl / 2))
elif forma == 4:
    qt = int(input('Em quantas vezes gostaria de parcela, em ate 10x: '))
    print('Parcelando em {} x o valor da parcela é de R${:.2f} com juros de 20%.'.format(qt,(vl + (vl * 20 / 100)) / qt))