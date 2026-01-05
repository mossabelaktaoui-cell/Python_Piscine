#!/usr/bin/env python3
class Plant:
    total_growth = 0
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__type = "regular"

    def grow(self):
        self.__height += 1
        Plant.total_growth += 1

    def set_height(self, new_height):
        if new_height >= 0:
            self.__height = new_height
        else:
            print("Warning: Height is invalid!")

    def get_info(self):
        print(f"- {self.name}: {self.__height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.__is_blooming = 0
        self.__type = "flowering"
    
    def bloom(self):
        self.__is_blooming = 1

    def get_info(self):
        if self.__is_blooming:
            print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)")
        if not self.__is_blooming:
            print(f"- {self.name}: {self.height}cm, {self.color} flowers")

class PrizePlant(FloweringPlant):
    def __init__(self,name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points
        self.__type = "prize"

    def get_info(self):
        if self.__is_blooming:
            print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.prize_point}")
        if not self.__is_blooming:
            print(f"- {self.name}: {self.height}cm, {self.color} flowers, Prize points: {self.prize_point}")
     
    
class Garden():
    plants_counter = 0
    def __init__(self, name):
        self.name = name
        self.plants = []
    
    def add_plant(self, new_plant):
        self.plants.append(new_plant)
        print(f"Added {new_plant.name} to {self.name}'s garden")
        plants_counter += 1
    
    def plants_grow(self):
        print(f"{self.name} is helping all plants grow")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    def count_plants_types(self):
            regular = 0
            flowering = 0
            prize_flowers = 0
            for plant in self.plants:
                if plant.type == "regular":
                    regular += 1
                elif plant.type == "flowering":
                    flowering += 1
                elif plant.type == "prize":
                    prize += 1
            print(f"Plants types: {regular} regular, {flowering} flowering, {prize} prize flowers")
    
    


class GardenManager():
    gardens_counter = 0
    def __init__(self):
        self.gardens = []


    def add_garden(self, garden):
        self.gardens.append(garden)
        print(f"Added {garden.name} successfully")
        GardenManager.gardens_counter += 1
    
    

    @classmethod
    def get_total_gardens(cls):
        print(f"Total gardens managed: {cls.gardens_counter}")

    class GardenStats:
        @staticmethod
        def calculate_scores():
            print("Garden scores - ", end = '')
            i = 1
            for garden in GardenManager.gardens:
                score = 0
                for plant in garden.plants:
                    score += plant.prize_points
                print(f"{garden.name}: {score}", end = '')
                if i < GardenManager.gardens_counter:
                    print(", ")
                    i += 1
                else:
                    print("\n")

        
            
        




if __name__ == "__main__":
    gardenmanager = GardenManager()
    alice = Garden("Alice")
    gardenmanager.add_garden(alice)
    bob = Garden("Bob")
    gardenmanager.add_garden(bob)
    moh = Garden("Moh")
    gardenmanager.add_garden(moh)
    gardenmanager.get_total_gardens()
    rose = Plant("Rose")
    alice.add_plant(rose)
    rose.grow()
    alice.plants_grow()