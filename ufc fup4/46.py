import re
f = input().lower()
f = re.sub(r"[^a-zA-Z]", " ", f)
f = f.replace(" ", "")
tamanho = len(f)
inverso = ""
for i in range(tamanho -1, -1, -1):
    inverso += f[i]
if f == inverso:
    print(True)
else:
    print(False)