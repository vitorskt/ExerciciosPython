def conversor(valor):
    return int(valor) / 10 ** 6


usuarios = []
arquivo = open('usuarios.txt', 'r')
for linha in arquivo.readlines():
    nome = linha[:16].strip()
    uso = int(linha[16:].replace('\n', ''))
    uso_mb = conversor(uso)
    usuarios.append((nome, uso_mb))
arquivo.close()


def percentual(nome, lista=usuarios):
    total = 0
    individual = 0
    for u in lista:
        total = total + u[1]
        if u[0] == nome:
            individual = u[1]
    return individual / total * 100


arquivo = open('relatorio.txt', 'w')
arquivo.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
arquivo.write(f"{'-'*65}\n")
arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
total = 0
for indice, u in enumerate(usuarios):
    total += u[1]
    porcentagem = percentual(u[0])
    arquivo.write(f'{indice+1}\t{u[0]}\t\t\t{u[1]:.2f} MB\t\t\t\t{porcentagem:.2f}%\n')
arquivo.write(f"Espaço total ocupado: {total:.3f} MB\n")
arquivo.write(f"Espaço médio ocupado: {total/len(usuarios):.3f} MB")
arquivo.close()