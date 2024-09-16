def achar(s):
    contador = 0
    for caractere in s:
        if caractere == '1':
            contador += 1
    return contador


string = input("")
print(achar(string))
