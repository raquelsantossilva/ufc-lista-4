soma = 0
for i in range(3):
    nota = float(input(""))

    if 0 <= nota <= 10:
        soma += nota
    else:
        print("Nota invalida")
        break
if 0 <= nota <= 10:
    media = soma/3
    print(f'{media:.2f}')


