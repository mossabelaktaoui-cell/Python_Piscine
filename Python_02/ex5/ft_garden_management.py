class GardenError(Exception):
    """Custom exception for garden errors."""
    pass


class Plant:
    def __init__(self, name, water_leverl, sunlight_hours):
        """Initialize a plant with name, water level, and sunlight hours."""
        self.name = name
        self.water_level = water_leverl
        self.sunlight_hours = sunlight_hours

    def check_plant_health(self):
        """Check if the plant's health parameters are within valid ranges."""
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
        """Initialize the garden manager with an
        empty plant list and water tank."""
        self.plants = []
        self.water_tank = 1

    def add_plants(self, plants_list):
        """Add a list of plants to the garden."""
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
        """Water all plants in the garden."""
        print("Watering plants...")
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
        """Test recovery from errors like an empty water tank."""
        print("\nTesting error recovery...")
        try:
            if self.water_tank <= 0:
                raise GardenError(
                    "Caught GardenError: Not enough water in tank"
                )
        except GardenError as e:
            print(e)
        print("System recovered and continuing...")


def test_garden_management():
    """Run a test of the garden management system."""
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 15, 3)
    potato = Plant("", 0, 0)
    garden_manager = GardenManager()
    garden_manager.add_plants([tomato, lettuce, potato])
    print()
    garden_manager.water_plants()
    print("\nChecking plant health...")
    tomato.check_plant_health()
    lettuce.check_plant_health()
    garden_manager.test_error_recovery()
    print("\nGarden management system test complete!")
