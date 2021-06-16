n = 0
cont = soma = maior = menor = 0
r = ''
while r != 'N':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar [S/N] ')).strip().upper()
    if menor <= 0:
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if r != 'S':
        print('Opção invalida!')
        r = 'N'
    cont += 1
    soma += n

print('Você digitou {} numeros e a média entres eles é {} '.format(cont, soma / cont))
print('O maior numero é {} e o menor é {}'.format(maior, menor))