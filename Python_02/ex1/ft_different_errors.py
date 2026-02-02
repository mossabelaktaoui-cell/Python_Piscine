def garden_operations(operation_type):
    if operation_type == "value_error":
        return int("hello")

    elif operation_type == "zero_div":
        return 5 / 0

    elif operation_type == "file_not_found":
        return open("messing_file.txt", 'r')

    elif operation_type == "key_error":
        data = {"plant1": "rose"}
        return data["missing_plant"]


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        garden_operations("value_error")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations("zero_div")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        garden_operations("file_not_found")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        print("Testing KeyError...")
        garden_operations("key_error")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        print("Testing multiple errors together...")
        for error_type in ["value_error", "zero_div",
                           "file_not_found", "key_error"]:
            garden_operations(error_type)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
