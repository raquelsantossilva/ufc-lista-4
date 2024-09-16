f = input()
new_f = ""
tamanho = len(f)
for i in range(tamanho):
    if f[i] == "0":
        new_f += "1"
    else:
        new_f += f[i]
print(new_f)