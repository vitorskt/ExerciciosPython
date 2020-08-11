import moeda108

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.metade(p))}')
print(f'O dobro de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.dobro(p))}')
print(f'Aumentando 10%, temos {moeda108.moeda(moeda108.aumentar(p,10))}')
print(f'Diminuindo 15%, temos {moeda108.moeda(moeda108.diminuir(p,15))}')

