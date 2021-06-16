n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero,[Digite 999, para parar]: '))
    if n != 999:
        cont += 1
        soma += n
print('Você digitou {} numeros a soma entre eles é igual a {}.'.format(cont, soma))
print('FIM')
