#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input('digite seu nome ').lower()
idade = int(input('digite sua idade '))
salario = float(input('valor do salario '))
sexo = input('digite seu sexo, [m]masculino e [f]feminino ').lower()
EC = input('Estado Civil, [s]solteiro [c]casado, [v]viúvo, [d]divorciado ').lower()

dados = dict(nome = nome, idade = idade, salario = salario, sexo = sexo, EC = EC)

print(f"Nome: {dados['nome']}")
print(f"Idade: {dados['idade']}")
print(f"salario: {dados['salario']}")
print(f"sexo: {dados['sexo']}")
print(f"EC: {dados['EC']}")

while len(nome) <= 3:
    print('nome muito pequeno')
    nome = input('digite seu nome ')
while idade < 0 or idade > 150:
    print('idade inválida')
    idade = int(input('digite sua idade '))
while sexo != 'm' and sexo != 'f':
    print('sexo inválido')
    sexo = input('digite seu sexo, [m]masculino e [f]feminino ')
while EC != 's' and EC != 'c' and EC != 'v' and EC != 'd':
    print('Estado Civil inválido')
    EC = input('Estado Civil, [s]solteiro [c]casado, [v]viúvo, [d]divorciado ')
