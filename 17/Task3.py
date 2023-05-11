"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""


class SpaceObject:
    def __init__(self, size):
        self.size = size


class Star(SpaceObject):
    def __init__(self, brightness):
        self.brightness = brightness

    def print_brightness(self):
        print("Яркость звезды:", self.brightness)


class Planet(SpaceObject):
    def __init__(self, size, population, population_growth):
        super().__init__(size)
        self.population_growth = population_growth
        self.population = population


    def account_population(self, year):
        print(f"Население земли через {year} лет:",self.population + year * self.population_growth)

Zemla = Planet(10,8000000000,1)

Zemla.account_population(3)

