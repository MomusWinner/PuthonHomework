
def is_magic_date(date:str):
    date = date.split('.')

    return True if int(date[0])*int(date[1]) == int(date[2][2:]) else False

print(is_magic_date("10.06.1960"))