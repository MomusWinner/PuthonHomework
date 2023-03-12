a = input()

if len(a) != len(set(a)):
    print("Есть похожие элементы")
else:
    print("Нет похожих элементов")