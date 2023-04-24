# -*- coding: utf-8 -*-
def decorate(func):
    def wrapper(value1,value2):
        print(f"Данная функция ввыводит все числа между {value1} и {value2} ")
        func(value1,value2)
    return wrapper


@decorate
def func(value1,value2):
    [print(i) for i in range(value1,value2) if i % 3 == 0]

func(2,9)

