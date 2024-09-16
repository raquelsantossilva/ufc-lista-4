n1 = float(input(""))
operacao = input('')
n2 = float(input(""))

if operacao == '+':
    print(f'{n1 + n2:.2f}')
elif operacao == '-':
    print(f'{n1 - n2:.2f}')
elif operacao == '*':
    print(f'{n1 * n2:.2f}')
else:
    print(f'{n1/n2:.2f}')
