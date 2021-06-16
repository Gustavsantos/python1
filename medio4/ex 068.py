from random import randint
count = 0
while True:
    print('-='*13)
    print('Lets go game par or ímpar')
    print('-='*13)
    options = ''
    while  options != 'P' and options != 'I':
        options = str(input('select a options [P/I] ')).strip().upper()[0]
    player = int(input('select a number: '))
    computer = randint(0,10)
    r = (player + computer)
    if options == 'P'and r % 2 == 0:
        print('-'*16)
        print(f'Computer select {computer} end you {player} the sum between them is {r}  is PAR.')
        print('-'*16)
        count += 1
    else:
        if options == 'I' and r % 2 == 1:
            print('-'*30)
            print(f'computer select {computer} end you {player} the sum between them is {r:2} is ÍMPAR.')
            print('-'*30)
            count += 1
        else:
            print(f'commputer select {computer} end you { player} the sum between them is {r:2}.')
            print(f'you loss end game.')
            print(f'you wins {count}')
            break
print('GAME OVER')