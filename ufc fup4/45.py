def funcao(f, qnt):
    tamanho = len(f)
    new_frase = ""
    for i in range(0, tamanho):
        letra = f[i]
        if letra != " ":
            indicel = ord(letra)
            cont = indicel + qnt
            if cont > 90:
                conta = indicel + qnt - 90 + 64
                indicel = conta
            else:
                indicel += qnt
            new_frase += chr(indicel)
        else:
            new_frase += " "
    return (new_frase)
