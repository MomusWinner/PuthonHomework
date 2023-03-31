def is_good_pass(password: str):
    return True if len(password) > 8 and password.lower() != password else False


print(is_good_pass("sdfsfF"))