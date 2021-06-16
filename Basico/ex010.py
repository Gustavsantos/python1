a=float(input('Qual a altura da sua parede?'))
l=float(input('Qual a largura da parade?'))
r=a*l
print('a area da sua parede é igual a {}x{}={}m²'.format(a,l,a*l))
print('voce precisara de {} litros de tinta para pintar {}m²'.format(r/2,r))