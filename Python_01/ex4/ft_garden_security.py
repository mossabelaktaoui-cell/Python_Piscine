#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
    
    def set_height(self, new_height: int):
        if new_height >= 0:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self):
        return self.__height
    
    def set_age(self, new_age: int):
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self):
        return self.__age

def ft_garden_security():
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)

    print (f"\nCurrent plant: {rose.name} ({rose.get_height()}cm, {rose.get_age()} days)")

if __name__ == "__main__":
    ft_garden_security()
