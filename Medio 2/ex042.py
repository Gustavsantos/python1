print('Digite três valores, para saber se eles podem formar um triangulo')
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor:  '))
v3 = float(input('Terceiro valor: '))
if  v1 + v2 > v3 and v2 + v3 > v1 and v3 + v1 > v2:
    print('Esses valores podem, formar um triangulo!')
    if v1 == v2 == v2:
        print('EQUILÁTERO')
    elif v1 != v2 != v3 != v1 :
         print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Esses valores não podem formar um triangulo!')