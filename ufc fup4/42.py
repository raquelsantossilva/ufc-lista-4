f = input()
tamanho = len(f)
cont = 0
for i in range(tamanho):
    if f[i] == " ":
        cont += 1
print(cont)