#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height = self.height + 1

    def age_(self):
        self.age = self.age + 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth():
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


if __name__ == "__main__":
    ft_plant_growth()
