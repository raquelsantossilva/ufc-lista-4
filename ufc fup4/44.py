f = input()
tamanho = len(f)
new_Frase = ""
for i in range(tamanho - 1, -1, -1):
    if f[i] != "a":
        if f[i] != "A":
            new_Frase += f[i]
        else:
            new_Frase += "*"
    else:
        new_Frase += "*"
print(new_Frase)