import math

w = float(input())
h = float(input())
expenditure = float(input())
liters_in_bottles= float(input())
percent = float(input())

square = w * h
print(round(w * h,2))

liters = square / expenditure
unused = liters * percent / 100
liters += unused

print(round(liters,2))

bottles = int(math.ceil(liters / liters_in_bottles))
print(bottles)

print(round((float(bottles) * liters_in_bottles) - liters, 2))