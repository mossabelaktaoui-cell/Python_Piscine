class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self,name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        shade_surface = (self.trunk_diameter * 0.01 / 2) ** 2 * 3.1415926535897 * 398
        print(f"{self.name} provides {shade_surface:.0f} square meters of shade")

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutritional_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}")
    
    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")


def ft_plant_type():
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    rose.get_info()
    rose.bloom()
    print()
    cactus = Flower("Cactus", 15, 18, "white")
    cactus.get_info()
    cactus.bloom()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    oak.get_info()
    oak.produce_shade()
    print()
    fern = Tree("Fern", 300, 370, 30)
    fern.get_info()
    fern.produce_shade()
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
    tomato.get_info()
    tomato.get_nutritional_value()
    print()
    potato = Vegetable("Potato", 20, 55, "winter", "vitamin d")
    potato.get_info()
    potato.get_nutritional_value()


if __name__ == "__main__":
    ft_plant_type()
