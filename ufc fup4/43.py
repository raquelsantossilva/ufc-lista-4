nome = input()
idade = int(input())
nome_new = nome
idade_new = idade

while True:
    nome1 = input()
    idade2 = int(input())
    if idade2 < 0:
        break
    if idade2 < idade_new:
        idade_new = idade2
        nome_new = nome1
    if idade2> idade:
        idade = idade2
        nome = nome1
print(f"{nome_new} \n{idade_new} \n{nome} \n{idade}")