def water_plants(plant_list):
    """Waters a list of plants and ensures the watering
    system is closed regardless of errors."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
        print("Watering completed successfully!\n")
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Tests the watering system with valid and invalid plant
    inputs to demonstrate finally block behavior."""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Testing with error...")
    water_plants(["tomato", None, None])
    print("\nCleanup always happens, ever with errors!")
