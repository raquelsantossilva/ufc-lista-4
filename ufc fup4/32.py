n1 = int(input(""))
n2 = int(input(""))

if n1 < n2:
    n1, n2 = n2, n1

i = 1
while n1 >= i * n2:
    i += 1

quociente = i - 1

print(quociente)