a = 700
b = 1000

while a != b:
    a, b = map(int, input().split())
    if a > b:
        print('Decrescente')
    elif a < b:
        print('Crescente')
