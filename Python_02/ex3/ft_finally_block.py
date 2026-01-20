def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print("\nTesting with error...")
    water_plants(["tomato", None, None])
    print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()
