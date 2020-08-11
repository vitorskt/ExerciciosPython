#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e
#devolva uma string no formato D de mesPorExtenso de AAAA.
#Opcionalmente, valide a data e retorne NULL caso a data seja inválida.


#dia, mês, ano = input('Data (dd/mm/aaaa): ').split('/')

#meses = ['janeiro','fevereiro','março','abril',
#         'maio','junho','julho','agosto','setembro',
#         'outubro','novembro','dezembro']


#print ('Você nasce em:')
#print (meses = ['janeiro','fevereiro','março','abril',
#         'maio','junho','julho','agosto','setembro',
#         'outubro','novembro','dezembro']')

def format_data(data):
    dia, mes, ano = data.split('/')
    meses = ['janeiro','fevereiro','março','abril',
         'maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro']
    return f'{dia} de {meses[int(mes)-1]} de {ano}'

print(format_data('20/04/2001'))
