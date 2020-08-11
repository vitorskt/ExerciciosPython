nome = input('Digite seu nome')
idade = int(input('Digite sua idade'))
cidade = input('Qual é sua cidade?')

dicionario = dict(nome = nome, idade = idade, cidade = cidade)#adicionei os valores das variaveis acima em um dicionário

print(f"Nome: {dicionario['nome']}")
print(f"Idade: {dicionario['idade']}")
print(f"Cidade: {dicionario['cidade']}")
