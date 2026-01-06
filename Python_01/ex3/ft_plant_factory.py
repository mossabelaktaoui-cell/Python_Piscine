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


data = [
    {"name": "Rose", "Height": 25, "Age": 30},
    {"name": "Oak", "Height": 200, "Age": 365},
    {"name": "Cactus", "Height": 5, "Age": 90},
    {"name": "Sunflower", "Height": 80, "Age": 45},
    {"name": "Fern", "Height": 15, "Age": 120}
]


def ft_plant_factory():
    """
    Create Plant objects from a predefined data list.
    Instantiates plants from dictionary data and displays
    creation details with a total count.
    """
    print("=== Plant Factory Output ===")
    i = 0
    for item in data:
        plant = Plant(item["name"], item["Height"], item["Age"])
        print(
            f"Created: {plant.name} ({plant.height}cm, {plant.age} days)"
            )
        i += 1
    print(f"\nTotal plants created: {i}")
