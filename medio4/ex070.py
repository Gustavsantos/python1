print('-'*14)
print('SHOPPING GUSTA')
print('-'*14)
smaller = 0
namesm = ''
total = 0
totalsm = 0
while True:
    product = str(input('Name product? ')).strip().capitalize()
    values = float(input('Value  product? $'))
    options = str(input('continued? [Y/N]. ')).strip().upper()
    while options not in 'YN':
        options = str(input('continued? [Y/N]. ')).strip().upper()
    total += values
    if smaller ==0:
        smaller = values
    if  values < smaller:
        smaller = values
        namesm = product
    if options == 'N':
        break
    if values >= 1000:
        totalsm += 1
print(f'totals values ${total:2}.')
print(f'Higher values of  $1000 there are product with that volue {totalsm}. ')
print(f'the lowest volue is ${smaller} is name product is {namesm}')

