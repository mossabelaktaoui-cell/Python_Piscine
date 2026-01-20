def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too low (min 1)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    data = [
        ("good values", "tomato", 5, 8),
        ("empty plant name", "", 5, 8),
        ("bad water level", "tomato", 15, 8),
        ("bad sunlight hours", "tomato", 5, 1)
        ]
    for status, name, water_level, sunlight_hours in data:
        try:
            print(f"\nTesting {status}...")
            check_plant_health(name, water_level, sunlight_hours)
        except ValueError as e:
            print(e)

    print("\nAll error raising tests completed!")

if __name__ == "__main__":
    test_plant_checks()
