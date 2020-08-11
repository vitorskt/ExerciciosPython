def hora(h,m):
  conversao = h / 12 #divide a hora por 12
  if conversao <= 1: #método de conversão
    hora1 = str(h)
    print(f'A hora é {hora1}:', end='')
  elif conversao > 1 and conversao < 2:
    hora2 = str(h-12)
    print(f'A hora é {hora2}:', end='')
  else:
    print('horário Inválido.')


  if conversao <= 0.99 and m <= 60: #saber se é AM ou PM
    print(f'{m} AM')
  elif conversao > 0.99 and m <= 60:
    print(f'{m} PM')
  else:
    print('Formato inválido.')


while True:
  horario = input('Digite a hora: ').split(':')#split para deixar no formato de hora
  h, m = horario 
  h = int(h) 
  m = int(m)

  hora(h,m)
    
