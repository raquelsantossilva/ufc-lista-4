soma = media = 0
i = 1
while True:
    if i > 10:
        break
    n = int(input(""))
    if n > 0:
        soma += n
        i += 1
    else:
        continue


media = soma/10
print(f'{media:.2f}')
