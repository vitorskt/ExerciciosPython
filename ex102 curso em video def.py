def fatorial(n, show=False):
    """
    -> Calcula o fatorial um número.
    :Param n: O número a ser calculado.
    :Param show: (Opcional) mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f

#programa principal
print(fatorial(5, show=True))
#help(fatorial)
            
