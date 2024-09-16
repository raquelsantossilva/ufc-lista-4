divisores = 0
n = int(input(""))

Nao = sim = False

for i in range(1, n+1):

    if n % i == 0:
        divisores += 1
        if divisores > 2 or n == 1:
            Nao = True
        else:
            sim = True


if Nao:
    print("Nao primo")
elif sim:
    print("Primo")
