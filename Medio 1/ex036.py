print('Ola esse é nosso sistema, que ira te ajudar,na analise do seu perfil\nMas antes preciso de algumas informações')
vc = float(input('Qual o valor, da casa que você, gostaria de financiar?'))
m = int(input('Você quer pagar, em quantos anos?'))
print('Para que o financiamento seja aprovado, você só pode comprometer 30% da sua renda mensal')
sl = float(input('Quanto você ganhar por mês?'))
vp = vc / (m * 12)
f = (sl * 30) / 100
if f < vp:
    print('Seu financiamento, não pode ser aprovado, o valor da parcela é de R$\033[32m{:.2f}\033[m e 30% da sua renda é igual a R$\033[31m{:.2f}\033[m!'.format(vp,f))
    print('Desculpe mas podemos aprovar seu financiamento')
else:
    print('Seu financimaneto foi aprovado, o valor da parcelo por mes é de R$\033[31m{:.2f}\033{m'.format(vp))