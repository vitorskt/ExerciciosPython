import sqlite3

print("CREATE = CT\n"
      "INSERT = IST\n"
      "READ = RD\n"
      "UPDATE = UPD\n"
      "DELETE = DLT\n"
      "ALTER TABLE (ADD COLUMN ou RENAME TO) = ALTB\n"
      "SAIR = 0")
while True:
    msg = input("Bem vindo ao sistema de bando de dados!\n"
                "O que deseja fazer?").lower()

    conn = sqlite3.connect('prova.db')
    cursor = conn.cursor()
    if msg == "ct":
        cursor.execute("""
        CREATE TABLE usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(50) NOT NULL,
                idade INTEGER,
                email TEXT NOT NULL);
        """)
        print("Tabela criada com sucesso")

    if msg == "ist":
        nome = input('Digite o NOME do usuario: ')
        idade = int(input('Digite a IDADE agora: '))
        email = input('Por ultimo o EMAIL: ')
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO usuarios (nome, idade, email)
        VALUES ('{nome}', {idade}, '{email}')
        """)
        conn.commit()
        print("dados inseridos com sucesso")

    elif msg == "rd":
        oq = input("O que deseja ler?")
        todos_ou_nao = input("Quer os dados de todos? ")
        if oq == 'tudo' or '*' and todos_ou_nao == 'sim' or 's':
            cursor = conn.cursor()
            for u in cursor.execute(f"SELECT * FROM usuarios;"):
                print(u)

        elif oq == 'tudo' or '*' and todos_ou_nao == 'nao' or 'n':
            quem = int(input("ID do usuario: "))
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM usuarios WHERE id={quem};")
        res = cursor.fetchall()
        print(res)

    elif msg == "upd":
        oq = input("O que deseja atualizar? ").lower()
        quem = int(input('ID do usuario: '))
        if oq == 'nome':
            name = input("Qual nome deseja colocar?")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE usuarios(nome) SET '{name}',' WHERE id={quem};")
            conn.commit()
            print("Atualizado com sucesso")

        elif oq == 'idade':
            year_old = input("Que idade deseja colocar?")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE usuarios(idade) SET '{year_old}',' WHERE id={quem};")
            conn.commit()
            print("Atualizado com sucesso")

        elif oq == 'email':
            eml = input("Qual Email deseja colocar?")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE usuarios SET email = '{eml}' WHERE id={quem};")
            conn.commit()
            print("Atualizado com sucesso")

        else:
            print('Comando não reconhecido')

    elif msg == "dlt":
        delete = int(input('qual id do usuario a ser deletado?'))
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM usuarios WHERE id = {delete}")
        conn.commit()
        print(f"Usuario de ID {delete} deletado com sucesso")

    elif msg == 'altb':
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

    elif msg == '0':
        break

conn.close()
