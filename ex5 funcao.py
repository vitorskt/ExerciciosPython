def somaImposto(taxaImposto, custo):
    taxaImposto = (Q_imp/100)*custo
    custo = V_prod + taxaImposto
    return(taxaImposto)
    return(custo)
Q_imp = float(input('digite a quantia de imposto: '))
V_prod = float(input('digite o custo do produto: '))

print(f'O valor do imposto é: {somaImposto(Q_imp,V_prod)}R$')
#print(f'O custo do produto com imposto é: {somaImposto(Q_imp,V_prod)}')
