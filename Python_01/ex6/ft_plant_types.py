#!/usr/bin/env python3
class Plant:
    """
    Base class representing a regular plant with basic attributes.
    Stores name, height, and type with growth capability.
    """
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.type = "regular"

    def grow(self):
        """
        Increase the plant's height by 1 centimeter.
        """
        self.height += 1

    def get_info(self):
        """
        Display the plant's name and height.
        """
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """
    Represents a flowering plant with color and blooming status.
    Inherits from Plant and adds flower-specific attributes.
    """
    def __init__(self, name, height, color, is_blooming):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming
        self.type = "flowering"

    def bloom(self):
        """
        Set the plant's blooming status to active.
        """
        self.is_blooming = 1

    def get_info(self):
        """
        Display the flowering plant's information
        """
        if self.is_blooming:
            print(f"- {self.name}: {self.height}cm, "
                  f"{self.color} flowers (blooming)")
        if not self.is_blooming:
            print(f"- {self.name}: {self.height}cm, {self.color} flowers")


class PrizePlant(FloweringPlant):
    """
    Represents a prize-winning flowering plant with points.
    Inherits from FloweringPlant and adds prize scoring capability.
    """
    def __init__(self, name, height, color, is_blooming, prize_points):
        super().__init__(name, height, color, is_blooming)
        self.prize_points = prize_points
        self.type = "prize"

    def get_info(self):
        """
        Display the prize plant's information including prize points.
        """
        if self.is_blooming:
            print(f"- {self.name}: {self.height}cm, {self.color} flowers "
                  f"(blooming), Prize points: {self.prize_points}")
        if not self.is_blooming:
            print(f"- {self.name}: {self.height}cm, {self.color} flowers, "
                  f"Prize points: {self.prize_points}")


class Garden():
    """
    Manages a collection of plants in a named garden.
    Tracks plants, growth, and provides reporting capabilities.
    """
    def __init__(self, name):
        self.name = name
        self.plants = []
        self.plants_counter = 0
        self.total_growth = 0

    def add_plant(self, new_plant):
        """
        Add a new plant to the garden and increment the plant counter.
        """
        self.plants.append(new_plant)
        print(f"Added {new_plant.name} to {self.name}'s garden")
        self.plants_counter += 1

    def plants_grow(self):
        """
        Increase the height of all plants in the garden by 1cm.
        """
        print(f"{self.name} is helping all plants grow")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")
        self.total_growth += 1 * self.plants_counter

    def count_plants_types(self):
        """
        Count and display the number of each plant type in the garden.
        """
        regular = 0
        flowering = 0
        prize_flowers = 0
        for plant in self.plants:
            if plant.type == "regular":
                regular += 1
            elif plant.type == "flowering":
                flowering += 1
            elif plant.type == "prize":
                prize_flowers += 1
        print(f"Plants types: {regular} regular, {flowering} flowering, "
              f"{prize_flowers} prize flowers")

    def report(self):
        """
        Generate a comprehensive report of the garden's status.
        """
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()
        print(f"\nPlants added: {self.plants_counter}, "
              f"Total growth: {self.total_growth}cm")
        self.count_plants_types()


class GardenManager():
    """
    Manages multiple gardens and provides network-level operations.
    Tracks total gardens with class variable and calculates scores.
    """
    gardens_counter = 0

    def __init__(self):
        """
        Initialize the garden management system.
        """
        print("=== Garden Management System Demo ===\n")
        self.gardens = []
        self.gardens_counter = 0

    def add_garden(self, garden):
        """
        Add a garden to the management system and increment counters.
        """
        self.gardens.append(garden)
        self.gardens_counter += 1
        GardenManager.gardens_counter += 1

    def create_garden_network(self, garden_list):
        """
        Add multiple gardens to the system from a list.
        """
        for garden in garden_list:
            self.add_garden(garden)

    @classmethod
    def get_total_gardens(cls):
        """
        Display the total number of gardens managed across all instances.
        """
        print(f"Total gardens managed: {cls.gardens_counter}")

    def calculate_scores(self):
        """
        Calculate and display scores for all gardens.
        Based on plant heights and prize points.
        """
        print("Garden scores - ", end='')
        i = 1
        for garden in self.gardens:
            score = 0
            for plant in garden.plants:
                score += plant.height
                if plant.type == "prize":
                    score += plant.prize_points
            print(f"{garden.name}: {score}", end='')
            if i < self.gardens_counter:
                print(", ", end='')
                i += 1
            else:
                print()

    class GardenStats:
        """
        Provides utility methods for garden statistics and validation.
        """
        @staticmethod
        def height_checker(height):
            """
            Validate if a given height value is non-negative.
            """
            if height >= 0:
                print("Height validation test: True")
            else:
                print("Height validation test: False")


# if __name__ == "__main__":
#     gardenmanager = GardenManager()
#     alice = Garden("Alice")
#     bob = Garden("Bob")
#     gardenmanager.create_garden_network([alice, bob])
#     oak_tree = Plant("Oak Tree", 100)
#     alice.add_plant(oak_tree)
#     rose = FloweringPlant("Rose", 25, "red", 1)
#     alice.add_plant(rose)
#     rose.bloom()
#     sunflower = PrizePlant("Sunflower", 50, "yellow", 1,  10)
#     alice.add_plant(sunflower)
#     sunflower.bloom()
#     print()
#     alice.plants_grow()
#     print()
#     alice.report()
#     print()
#     GardenManager.GardenStats.height_checker(rose.height)
#     gardenmanager.calculate_scores()
#     gardenmanager.get_total_gardens()
