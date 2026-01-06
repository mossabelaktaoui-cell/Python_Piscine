#!/usr/bin/env python3
class Plant:
    """
    Represents a plant with basic attributes.
    Stores the plant's name, height in centimeters, and age in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():
    """
    Create and display a registry of plants in the garden.
    Instantiates multiple Plant objects and prints their
    details in a formatted list.
    """
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    for plant in (rose, sunflower, cactus):
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
