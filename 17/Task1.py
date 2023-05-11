"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""
class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor

    def print_info(self):
        print('Уровень здоровья', self.health)
        print('Класс брони', self.armor, "\n")

class Magician(Hero):
    def hello(self):
        print('Я армянский маг Арег.')
        super().print_info()

    def attack(self, enemy:Hero):
        damage = 10000 - enemy.armor
        print(f"Маг красавчик атакует {enemy.name} и наносит ему {damage}урона")
        enemy.health -= damage
        print(f"Здоровье врага {enemy.health}")


kaplan = Hero("Каплан",0.1,1000000000)
areg = Magician("Арег",100000000,1000000000)
areg.attack(kaplan)