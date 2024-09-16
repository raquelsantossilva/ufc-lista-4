n1 = float(input(""))
n2 = float(input(''))
n3 = float(input(""))
while True:
    if n1 >= n2 and n1 >= n3:
        print(f'{n1:.2f}')
        break
    elif n2 >= n1 and n2 >= n3:
        print(f'{n2:.2f}')
        break
    elif n3 >= n1 and n3 >= n2:
        print(f'{n3:.2f}')
        break
