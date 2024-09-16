def simplificar(num, den):
    teste = num
    if num > den:
        teste = den
    maior = 0
    for i in range(1, teste + 1):
        if num % i == 0:
            if den % i == 0:
                maior = i

    a = num // maior
    b = den // maior
    return a, b
