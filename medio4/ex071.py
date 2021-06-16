print ('-'*15)
print('{:^30}' .format('BANC NY'))
print( '-'*15)
count = 0
c = 0
cont10 = 0
cont1 = 0
value = int(input('what amount would  you like  to wirthdraw: $ '))
while True:
    if value >= 50:
        value -= 50
        count += 1
    else:
        if value >= 20:
            value -= 20
            c += 1
        else:
            if value >= 10:
                value -= 10
                cont10 += 1
            else:
                value -= 1
                cont1 += 1
    if value == 0:
        break
print(f'Will get {count}  $50 notes. ')
print(f'Will get {c} $20 notes.')
print(f'Will get {cont10} $10 notes.')
print(f'Will get {cont1} $1 notes.')
print('thanks for using  NY BANK')