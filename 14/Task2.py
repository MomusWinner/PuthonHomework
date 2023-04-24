def decorate(func):
    def wrapper():
        func()
        print("\nСалат\nАнанас")
    return wrapper()

@decorate
def func():
    print("Ингредиенты бургера \nМясо\nБулочка\nОгурчики")
