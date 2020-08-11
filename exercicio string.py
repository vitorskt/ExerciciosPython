p1 = input('escreva uma palavra')
p2 = input('escreva outra paalvra')

print(f'STRING 1: {p1}')
print(f'Tamanho de "{p1}": {len(p1)} caracteres')

print(f'STRING 2: {p2}')
print(f'Tamanho de "{p2}": {len(p2)} caracteres')

if len(p1) == len(p2):
      print('As duas strings são do mesmo tamanho')
else:
    print('As duas strings são de diferentes tamanhos')

if p1 == p2:
      print('As duas strings possuem o mesmo conteúdo')
else:
    print('As duas strings possuem conteúdos diferentes')
      
