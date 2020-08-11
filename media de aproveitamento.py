print('Média de Aproveitamento')

nota1 = float(input('Sua primeira nota'))
nota2 = float(input('Sua segunda nota'))
resultado = nota1 + nota2 #calculo da média
resultado = resultado/2

print("""Conceito de Avaliação:
    A: Ótimo
    B: Bom
    C: Médio
    D: Ruim
    E: Péssimo""")

while resultado > 10: #enquanto a média for maior que 10, repete o código
    print('== Nota inválida!!! ==')
    nota1 = float(input('Sua primeira nota'))
    nota2 = float(input('Sua segunda nota'))

if resultado >= 8: #condições para o aprovamento ou reprovamento
    print('Você foi Aprovado com aproveitamento "A"')
elif resultado >= 7:
    print('Você foi Aprovado com Aproveitamento "B"')
elif resultado >= 6:
    print('Você foi Aprovado com Aproveitamento "C"')
elif resultado >= 4:
    print('Vocêfoi Reprovado com Aproveitamento "D"')
elif resultado >= 0:
    print('Vocêfoi Reprovado com Aproveitamento "E"')

print(f'Sua média é {resultado:.2f}')#resultado da média com apenas duas casas decimais
