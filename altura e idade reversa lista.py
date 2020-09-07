lista_alt = []
lista_id = []

for res in range(5):
    altura = float(input('digite sua altura'))
    lista_alt.append(altura)

for res in range(5):
    idade = int(input('Digite sua idade'))
    lista_id.append(idade)

lista_alt.reverse()
lista_id.reverse()
print(f'A altura das pessoas inversa1.s é {lista_alt}')
print(f'A idade das pessoas inversas é {lista_id}')
