## Выводит большее число
x = int(input())
y = int(input())
c = (((x - y) // (x * y)) + 1) * x
v = (((y - x) // (x * y)) + 1) * y
print(c + v)
