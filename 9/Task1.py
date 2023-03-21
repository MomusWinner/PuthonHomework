"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def function(value1, value2, value3):
    if value2 is None or value1 is None or value3 is None:
        print("Один из объектов None")
    else:
        print(value1, value2, value3)

function("value1", "value2", None)