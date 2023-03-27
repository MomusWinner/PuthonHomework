import gym_inf
import str_control

string = input("Введите запрос(off отменить): ").lower()
while string != "off":
    print(f"---------\nКоличество слов: {str_control.counting_words(string)}\n---------")
    str_control.keyword_search(string)
    string = input("Введите запрос(off отменить): ").lower()
