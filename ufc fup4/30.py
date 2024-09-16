n = int(input())
maior = -99999
cont = 0
for i in range(n):
  x = int(input())
  if x > maior:
    maior = x
    cont = 1
  elif x == maior:
    cont += 1
print(maior)
print(cont)