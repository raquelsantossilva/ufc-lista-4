for i in range(1000, 10000):
    temp = i
    u = 0
    d = 0
    c = 0
    m = 0

    u = temp % 10
    temp //= 10
    d = temp % 10
    temp //= 10
    c = temp % 10
    temp //= 10
    m = temp % 10

    n1 = u + d * 10
    n2 = c + m * 10

    soma = n1 + n2

    resultado = soma ** 2

    if resultado == i:
        print(i)