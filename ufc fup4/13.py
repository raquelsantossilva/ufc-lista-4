from math import sqrt

a = float(input(""))
if a == 0:
    print("Nao eh equacao do 2o grau")

b = float(input(""))
c = float(input(""))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Nao existe raiz real")

if a != 0 and delta > 0:
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    raiz2 = (-b - sqrt(delta)) / (2 * a)
    print(f"{raiz1:.2f}\n{raiz2:.2f}")
elif delta == 0:
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    print(f'{raiz1:.2f}')
    print("Raiz unica")
