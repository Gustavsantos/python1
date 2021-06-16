print('Digite tres valores, para saber se eles podem formar um triagulo')
v1 = float(input('Primeiro valor:'))
v2 = float(input('Segundo valor:'))
v3 = float(input('O ultimo valor'))
if v1 < v2 + v3 and v2 < v3 + v1 and v3 < v2+ v1:
    print('É possivel montar um triangulo com esses valores!')
else:
    print('Não é possivel montar um triangulo com esses valores!')

