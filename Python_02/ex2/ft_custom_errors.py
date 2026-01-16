class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_water_tank(level):
    if level < 5:
        raise WaterError("Not enough water in the tank!")


def check_plant_watering(days, plant):
    if days > 3:
        raise PlantError(f"The {plant} plant is wilting!")


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        check_plant_watering(5, "tomato")
    except GardenError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        check_water_tank(4)
    except GardenError as e:
        print(f"Caught WaterError: {e}\n")
    try:
        print("Testing catching all garden errors...")
        check_plant_watering(5, "tomato")
    except PlantError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water_tank(4)
    except WaterError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")
