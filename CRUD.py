import sqlite3

print("CREATE = CT\n"
      "INSERT = IST\n"
      "READ = RD\n"
      "UPDATE = UPD\n"
      "DELETE = DLT\n"
      "ALTER TABLE (ADD COLUMN ou RENAME TO) = ALTB\n"
      "SAIR = 0")
while True:
    messenger = input("Bem vindo ao sistema de banco de dados!\nO que deseja fazer? ").lower()

    conn = sqlite3.connect('prova.db')
    cursor = conn.cursor()
    if messenger == "ct":
        cursor.execute("""
        CREATE TABLE usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(50) NOT NULL,
                idade INTEGER,
                email TEXT NOT NULL);
        """)
        print("Tabela criada com sucesso")

    if messenger == "ist":
        nome = input('Digite o NOME do usuario: ')
        idade = int(input('Digite a IDADE agora: '))
        email = input('Por ultimo o EMAIL: ')
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO usuarios (nome, idade, email)
        VALUES ('{nome}', {idade}, '{email}')
        """)
        conn.commit()
        print("dados inseridos com sucesso")
        conn.close()

    elif messenger == "rd":
        ler = input("O que deseja ler? ").strip().lower()
        todos_ou_nao = input(f"De todos os usuarios? ").strip().lower()

        if ler == 'nome' and todos_ou_nao == 'sim' or todos_ou_nao == 's':
            cursor = conn.cursor()
            [print(u) for u in cursor.execute(f"SELECT nome FROM usuarios;")]

        elif ler == 'nome' and todos_ou_nao == 'nao' or todos_ou_nao == 'n':
            pessoa = int(input("Digite o ID do usuario: "))
            cursor = conn.cursor()
            cursor.execute(f"SELECT nome FROM usuarios WHERE id={pessoa};")

        elif ler == 'idade' and todos_ou_nao == 'sim' or todos_ou_nao == 's':
            cursor = conn.cursor()
            [print(u) for u in cursor.execute(f"SELECT idade FROM usuarios;")]

        elif ler == 'idade' and todos_ou_nao == 'nao' or todos_ou_nao == 'n':
            pessoa = int(input("Digite o ID do usuario: "))
            cursor = conn.cursor()
            cursor.execute(f"SELECT idade FROM usuarios WHERE id={pessoa};")

        elif ler == 'email' and todos_ou_nao == 'sim' or todos_ou_nao == 's':
            cursor = conn.cursor()
            [print(u) for u in cursor.execute(f"SELECT email FROM usuarios;")]

        elif ler == 'email' and todos_ou_nao == 'nao' or todos_ou_nao == 'n':
            pessoa = int(input("Digite o ID do usuario: "))
            cursor = conn.cursor()
            cursor.execute(f"SELECT email FROM usuarios WHERE id={pessoa};")
        res = cursor.fetchall()
        print(res)

    elif messenger == "upd":
        ler = input("O que deseja atualizar? ").lower()
        quem = int(input('ID do usuario: '))
        if ler == 'nome':
            name = input("Qual nome deseja colocar?")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE usuarios SET nome = '{name}' WHERE id={quem};")
            conn.commit()
            print("Atualizado com sucesso")

        elif ler == 'idade':
            year_old = input("Que idade deseja colocar?")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE usuarios SET idade = '{year_old}' WHERE id={quem};")
            conn.commit()
            print("Atualizado com sucesso")

        elif ler == 'email':
            eml = input("Qual Email deseja colocar?")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE usuarios SET email = '{eml}' WHERE id={quem};")
            conn.commit()
            print("Atualizado com sucesso")

        else:
            print('Comando não reconhecido')

    elif messenger == "dlt":
        delete = int(input('qual id do usuario a ser deletado?'))
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM usuarios WHERE id = {delete}")
        conn.commit()
        print(f"Usuario de ID {delete} deletado com sucesso")

    elif messenger == 'altb':
        mudanca = input("Qual a mudança? ex: RENAME TO ").lower()
        if mudanca == 'add column':
            novo = input("nome da coluna: ")
            esp = input("definicoes? ex: not null primary key autoincrement ")
            cursor = conn.cursor()
            cursor.execute(f"ALTER TABLE usuarios {mudanca} {novo} {esp};")
            print("Adicionado com sucesso")

        elif mudanca == 'rename to':
            qual = input("Qual a coluna que deseja mudar o nome? ")
            novo = input("Novo nome: ")
            cursor = conn.cursor()
            cursor.execute(f"ALTER TABLE usuarios RENAME COLUMN {qual} TO {novo};")
            print("Alterado com sucesso")

    elif messenger == '0':
        break

conn.close()
