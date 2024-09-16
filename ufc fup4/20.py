def funcao(n):
    raiz = n ** 0.5
    fat = raiz // 1
    res = fat ** 2
    if res == n:
        return True
    else:
        return False