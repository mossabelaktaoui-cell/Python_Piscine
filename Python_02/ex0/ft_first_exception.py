"""
Garden Temperature Checker

Validates temperature inputs for plant care, ensuring they fall within
the optimal range (0-40°C). Demonstrates exception handling for invalid inputs.
"""
print("=== Garden Temperature Checker ===\n")
i = 0
while i < 4:
    try:
        input_ = input("Testing temperature: ")
        temperature = int(input_)
        if temperature <= 40 and temperature >= 0:
            print(f"Temperature {temperature}°C is perfect for plants!\n")
        elif temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)\n")
    except ValueError:
        print(f"Error '{input_}' is not a valid number\n")
    i += 1
print("All tests completed - program didn't crash!")
