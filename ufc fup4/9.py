a = int(input(''))
b = int(input(''))
c = int(input(''))

if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
if a < b:
    a, b = b, a

print(f'{c}\n{b}\n{a}')
