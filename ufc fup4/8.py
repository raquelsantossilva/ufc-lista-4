n1 = float(input(""))
n2 = float(input(""))

resp = int(input(""))
while True:

    if resp == 1:
        print(f'{(n1 + n2) / 2:.2f}')
        break
    elif resp == 2:
        if n1 > n2:
            print(f'{n1 - n2:.2f}')
        else:
            print(f'{n2 - n1:.2f}')
        break
    elif resp == 3:
        print(f'{n1 * n2:.2f}')
        break
    elif resp == 4:
        if n2 == 0:
            print("Erro")
            break
        else:
            print(f'{n1 / n2:.2f}')
            break
    else:
        print('Erro')
        break