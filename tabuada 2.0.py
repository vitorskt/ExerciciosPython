from time import sleep
num = int(input('digite um número'))
for soma in range(1,11):
    print(f'{num}x{soma} = {num*soma}')
    sleep(0.5)
