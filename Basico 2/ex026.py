frase = str(input('Digite uma frase')).strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A letra "A" aparece a primeira vez na possição {}'.format(frase.upper().find('A')+1))
print('A letra "A" é utilizada a ultima vez na posição {}'.format(frase.rfind('a')+1))