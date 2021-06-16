cont = soma = 0
while True:
    n = int(input('enter a number.[999 is stop] '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'you typed {cont} numbers end the sum batween the is {soma}')