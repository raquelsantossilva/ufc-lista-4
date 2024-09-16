
while True:
    print("1 - Adicao\n"
          "2 - Subtracao\n"
          "3 - Multiplicacao\n"
          "4 - Divisao\n"
          "5 - Saida")
    res = int(input(""))
    if res == 5:
        break
    n1 = float(input(""))
    n2 = float(input(""))

    if res == 1:
        print(f'{n1+n2:.2f}')
    elif res == 2:
        print(f'{n1-n2:.2f}')
    elif res == 3:
        print(f'{n1*n2:.2f}')
    elif res == 4:
        print(f'{n1/n2:.2f}')

