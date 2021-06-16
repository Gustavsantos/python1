s = int(input('Digite o valor do seu salario, para seber o seu aumento:'))
a = 15
b = 10
p = (s * a) //100
if s>1250:
    p = s * b /100
r = p + s
if s>1250:
    print('Seu salario com o  aumento de {}% é igual R${:.2f}'.format(b,r))
else:
    print('Seu salario com o aumento de {}% é igual R${:.2f}'.format(a,r))