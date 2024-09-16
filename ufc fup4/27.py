q = int(input(""))
numero = float(input(""))
maior = menor = numero
for i in range(q-1):
    numero = float(input(""))
    if numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero

print(f'{menor:.2f}')
print(f'{maior:.2f}')
