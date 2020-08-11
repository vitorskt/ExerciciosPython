letras = []
vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(0, 10):
    letras.append(input('informe um caracter: ').lower())
totconsoantes = 0
consoantes = []

for i in range(0, 10):
    if letras[i] not in vogais:
        consoantes.append(letras[i])
        totconsoantes += 1
print(f'Você digitou {totconsoantes} consoantes')
print(consoantes)
