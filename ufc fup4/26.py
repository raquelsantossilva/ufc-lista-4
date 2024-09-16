n = float(input(""))
maior = menor = n

for i in range(9):
    n = float(input(""))
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'{menor:.2f}')
print(f'{maior:.2f}')