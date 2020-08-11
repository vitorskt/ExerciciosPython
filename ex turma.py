meses = ['janeiro','fevereiro','março','abril',
         'maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro']
def format_data(dia,mes,ano):
#meses = ['janeiro','fevereiro','março','abril',
#         'maio','junho','julho','agosto','setembro',
#         'outubro','novembro','dezembro']
    return f'{dia} de {meses[int(mes)-1]} de {ano}'

x = input('dia: ')
y = input('mes: ')
z = input('ano: ')
print(format_data(x, y, z))
