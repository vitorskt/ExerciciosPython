def contar_caracteres(s):
    """[Função que conta quantas vezes o caractere aparece na string]

    Args:
        s ([str]): [Palavra de entrada do usuario]
    """

    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior} : {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior} : {contagem}')


contar_caracteres('yeeshua')