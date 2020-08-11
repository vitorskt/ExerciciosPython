from time import sleep

valor = 1.99
x = 1
for num in range(50):
    print(f'{x*valor:.2f}')
    x += 1
    sleep(0.5)
