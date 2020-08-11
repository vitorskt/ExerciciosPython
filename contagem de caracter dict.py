def contar_caracteres(s):
    """[Função que conta quantas vezes o caractere aparece na string]

    Args:
        s ([str]): [Palavra de entrada do usuario]
    """

    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem
    
    return resultado


print(contar_caracteres('AATROX'))

# FORMA MAIS COMPLEXA:



"""    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    
    return resultado

print(contar_caracteres('AATROX'))"""