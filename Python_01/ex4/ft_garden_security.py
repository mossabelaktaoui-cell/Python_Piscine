#!/usr/bin/env python3
class SecurePlant:
    """
    Represents a plant with secure private attributes and validation.
    Prevents invalid values for height and age through setter validation.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, new_height: int):
        """
        Set the plant's height with validation to reject negative values.
        """
        if new_height >= 0:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self):
        """
        Return the plant's current height in centimeters.
        """
        return self.__height

    def set_age(self, new_age: int):
        """
        Set the plant's age with validation to reject negative values.
        """
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age "
                  f"{new_age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self):
        """
        Return the plant's current age in days.
        """
        return self.__age


def ft_garden_security():
    """
    Demonstrate the secure plant validation system.
    Creates a plant and tests valid and invalid
    attribute updates with security checks.
    """
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)

    print(f"\nCurrent plant: {rose.name} ("
          f"{rose.get_height()}cm, {rose.get_age()} days)")
