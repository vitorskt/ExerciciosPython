popA = int(input('Digite a população do primeiro país'))
popB = int(input('Digite a população do segundo país'))
anos = 0
cresA = float(input('Digite a taxa de crescimento do primeiro pais'))
cresA = cresA/100
cresB = float(input('Digite a taxa de crescimento do segundo o país'))
cresB = cresB/100
while popA < popB:
    anos += 1
    popA = popA + (popA*cresA)
    popB = popB + (popB*cresB)

print(f'Após {anos} anos o país A ultrapassou o país B em números de habitantes')
print(f'País A: {popA:.0f}')
print(f'País B: {popB:.0f}')
