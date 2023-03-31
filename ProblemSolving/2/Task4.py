db = {}


def write_student(name:str, count:int):
    db[name] = count


def find_student(name:str):
    print(db[name])


write_student("Areg", 5)

find_student("Areg")
