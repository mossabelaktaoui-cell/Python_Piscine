class Plant:
    """
    Base class representing a plant with fundamental attributes.
    Stores the plant's name, height in centimeters, and age in days.
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Represents a flowering plant with color attribute.
    Inherits from Plant and adds blooming capability.
    """
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Display a blooming message for the flower.
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        """
        Display the flower's information including name,
        height, age, and color.
        """
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")


class Tree(Plant):
    """
    Represents a tree with trunk diameter attribute.
    Inherits from Plant and can calculate shade area.
    """
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculate and display the shade area provided by the tree.
        """
        shade_surface = self.trunk_diameter ** 2 * 0.03125
        print(f"{self.name} provides "
              f"{shade_surface:.0f} square meters of shade")

    def get_info(self):
        """
        Display the tree's information including name,
        height, age, and trunk diameter.
        """
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a vegetable with harvest season and nutritional value.
    Inherits from Plant and provides nutritional information.
    """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutritional_value(self):
        """
        Display the nutritional value of the vegetable.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        """
        Display the vegetable's information including name,
        height, age, and harvest season.
        """
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")

# if __name__ == "__main__":
#     print("=== Garden Plant Types ===")
#     print()
#     rose = Flower("Rose", 25, 30, "red")
#     rose.get_info()
#     rose.bloom()
#     print()
#     cactus = Flower("Cactus", 15, 18, "white")
#     cactus.get_info()
#     cactus.bloom()
#     print()
#     oak = Tree("Oak", 500, 1825, 50)
#     oak.get_info()
#     oak.produce_shade()
#     print()
#     fern = Tree("Fern", 300, 370, 30)
#     fern.get_info()
#     fern.produce_shade()
#     print()
#     tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
#     tomato.get_info()
#     tomato.get_nutritional_value()
#     print()
#     potato = Vegetable("Potato", 20, 55, "winter", "vitamin d")
#     potato.get_info()
#     potato.get_nutritional_value()
