#!/usr/bin/env python3
class Plant:
    """
    Represents a plant with growth and aging capabilities.
    Tracks name, height in centimeters, and age in days with update methods.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """
        Increase the plant's height by 1 centimeter.
        """
        self.height = self.height + 1

    def age_(self):
        """
        Increase the plant's age by 1 day.
        """
        self.age = self.age + 1

    def get_info(self):
        """
        Display the plant's current information (name, height, and age).
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth():
    """
    Simulate plant growth over a week period.
    Creates a plant, tracks its growth, and displays before/after information.
    """
    rose = Plant("Rose", 25, 30)
    before = rose.height
    print("=== Day 1 ===")
    rose.get_info()
    i = 0
    while i < 6:
        rose.grow()
        rose.age_()
        i += 1
    print("=== Day 7 ===")
    rose.get_info()
    difference = rose.height - before
    print(f"Growth this week: +{difference}cm")
