escrito = ('zero', 'um','dois','trés', 'quatro', 'cinco', 'seis', ' sete' , 'oito' ,'nove' ,'déz', 'onze','doze','treze','quartoze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte' )
n = 21
while  True:
    n = int(input('Digite um numero para receber ele por extenso! '))
    if n <= 20  and n >= 0:
        break
    else:
        print('Opção invalida')

print(f'Você digitou {n} e escreve-se {escrito[n]}')