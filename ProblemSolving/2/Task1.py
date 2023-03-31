def is_triangle(a, b, c):
    return True if (a-b-c)*(b-c-a)*(c-b-a) <= 0 else False

print(is_triangle(58,48,12))