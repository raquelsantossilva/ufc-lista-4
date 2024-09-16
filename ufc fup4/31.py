n1 = int(input(""))
n2 = int(input(""))

soma_par = 0
mult_impar = 1

if n1 > n2:
    n1, n2 = n2, n1

for i in range(n1, n2 + 1):
    if i % 2 == 0:
        soma_par += i
    else:
        mult_impar *= i

print(f"{soma_par}")
print(f"{mult_impar}")
