def aumentar(preço=0, taxa=0,formato=False):
    """
    -> Função para aumentar o preço.
    :Param Preço: Preço a ser digitado pelo usuario.
    :Param Taxa: Taxa de aumento a ser escolhido.
    :Param Formato: Mostrar ou não o formato em Reais(R$)
    """
    res = preço + (preço*taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Função para diminuir o preço.
    :Param Preço: Preço a ser digitado pelo usuario.
    :Param Taxa: Taxa do desconto a ser escolhido.
    :Param Formato: Mostrar ou não o formato em Reais(R$)
    """
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0, formato=False):
    """
    -> Função para dobrar o preço.
    :Param Preço: Preço a ser digitado pelo usuario.
    :Param Formato: Mostrar ou não o formato em Reais(R$)
    """
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço=0, formato=False):
    """
    -> Função para pegar a metade do preço.
    :Param Preço: Preço a ser digitado pelo usuario.
    :Param Formato: Mostrar ou não o formato em Reais(R$)
    """
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço=0, moeda='R$'):
    """
    -> Função para transformar o preço em R$.
    :Param Preço: Preço a ser digitado pelo usuario.
    :Param Moeda: Transforma o preco em R$.
    """
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preco=0, taxaA=10, taxaR=5):
    print('-' * 33)
    print('RESUMO DO VALOR'.center(33))
    print('-' * 33)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'Com {taxaA}% de aumento: \t{aumentar(preco,taxaA,True)}')
    print(f'Com {taxaR}% de redução: \t{diminuir(preco,taxaR,True)}')
    print('-' * 33)