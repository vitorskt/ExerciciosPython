from moeda import diminuir, aumentar, metade, dobro

p = float(input('Digite um preço: R$'))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p,10)}')
print(f'Diminuindo 15%, temos {diminuir(p,15)}')

