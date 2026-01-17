class GardenError(Exception):
    pass


class Plant:
    def __init__(self, name, water_leverl, sunlight_hours):
        self.name = name
        self.water_level = water_leverl
        self.sunlight_hours = sunlight_hours

    def check_plant_health(self):
        try:
            if self.name == "":
                raise GardenError("Error: Plant name cannot be empty!")
            if self.water_level < 1 or self.water_level > 10:
                raise GardenError(
                    f"Error checking {self.name}: Water level "
                    f"{self.water_level} is too high (max 10)"
                )
            if self.sunlight_hours < 2 or self.sunlight_hours > 12:
                raise GardenError(
                    "Error: Sunlight hours 0 is too low (min 2)"
                )
            print(
                f"{self.name}: healthy (water: {self.water_level}, "
                f"sun: {self.sunlight_hours})"
            )
        except GardenError as e:
            print(e)


class GardenManager:
    def __init__(self):
        self.plants = []
        self.water_tank = 1

    def add_plants(self, plants_list):
        for plant in plants_list:
            try:
                if plant.name == "":
                    raise GardenError(
                        "Error adding plant: Plant name cannot be empty!"
                    )
                self.plants.append(plant)
                print(f"Added {plant.name} successfully")
            except GardenError as e:
                print(e)

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant.water_level += 1
                print(f"Watering {plant.name} - success")
            self.water_tank -= 1
        except GardenError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def test_error_recovery(self):
        try:
            if self.water_tank <= 0:
                raise GardenError(
                    "Caught GardenError: Not enough water in tank"
                )
        except GardenError as e:
            print(e)
        print("System recovered and continuing...")


def test_garden_management():
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 16, 3)
    potato = Plant("", 0, 0)
    garden_manager = GardenManager()
    garden_manager.add_plants([tomato, lettuce, potato])
    print("\nWatering plants...")
    garden_manager.water_plants()
    print("\nChecking plant health...")
    tomato.check_plant_health()
    lettuce.check_plant_health()
    print("\nTesting error recovery...")
    garden_manager.test_error_recovery()
    print("\nGarden management system test complete!")
