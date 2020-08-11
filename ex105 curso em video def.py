def notas(*n, sit=False):
    """
    -> Função para analisar notas de vários alunos.
    :Param n: Uma ou mais notas dos alunos.
    :Param sit: (OPCIONAL) mostra a situação em que se encontra o aluno.
    :Return: Dicionário com várias informacões sobre a situação do aluno.
    """
    r= dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa principal
resp = notas(8,6,7,9,5,sit=True)
print(resp)
#help(notas)
