def printar(x):
  i=1
  impressao = str(i)
  print(i)
  while i<=x:
    if i>1:
      impressao = impressao + str(i)
      print(impressao)
    i += 1
numero = int(input('digite um numero: '))
printar(numero)
