count = countm = countw = 0
while True:
    print('register a person')
    age = int(input('How old are you ? '))
    sex = ''
    while sex != 'M' and sex != 'W':
        sex = str(input('Your sex? [M/W] ')).strip().upper()
    options = str(input('Want to continued? [Y/N] ')).strip().upper()
    while options not in 'YN':
        options = str(input('Want to continued? [Y/N] ')).strip().upper()
    if sex =='W' and age >= 20:
        countw += 1
    if age >= 18:
        count +=1
    if sex == 'M':
        countm += 1
    if options == 'N':
        break


print(f'{count} People are  ouver 18 years old. ')
print(f'Total mens. {countm}')
print(f'Total womans over the age of  20. {countw}')
