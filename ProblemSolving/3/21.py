class Animal:
    def __init__(self, type, voice):
        self.type = type
        self.voice = voice

    def make_voice(self):
        print(f"Животное делает {self.voice}")

    def print_type(self):
        print(f"Животное конкретное {self.type}")



dog = Animal("Млекопитающее","Гаффффффф")
dog.make_voice()
dog.print_type()

cat = Animal("Млекопитающее","Мээээээ на")
cat.make_voice()