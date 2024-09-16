maior = menor = 0
algum_positivo = False
while True:
    n = int(input(""))
    if n < 0:
        break
    else:
        algum_positivo = True
    if maior == 0 and menor == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif 0 <= n < menor:
        menor = n
if algum_positivo:
    print(maior)
    print(menor)
