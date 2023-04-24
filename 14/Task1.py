from time import time

def decorate(func_to_decor):
    def wrapper():
        start_time = time()
        func_to_decor()
        print(time()-start_time)
    return wrapper()

@decorate
def func_to_decor():
    for i in range(1000):
        print(i)

func_to_decor()