def funcao(x1,x2):
    tam = len(x1)
    if x2 < x1:
        tam = len(x2)
    for i in range(tam):
        car1 = x1[i]
        car2 = x2[i]
        if car1 != car2:
            return False
    return True