def check_temperatures(temp_str):
    try:
        temperature = int(temp_str)
        if 0 <= temperature <= 40:
            return f"Temperature {temperature}°C is perfect for plants!\n"
        elif temperature > 40:
            return f"Error: {temperature}°C is too hot for plants (max 40°C)\n"
        else:
            return f"Error: {temperature}°C is too cold for plants (min 0°C)\n"
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    for temp in ["25", "abc", "100", "-50"]:
        print(f"Testing temperature: {temp}")
        result = check_temperatures(temp)
        if result:
            print(result)

    print("All tests completed - program didn't crash!")
