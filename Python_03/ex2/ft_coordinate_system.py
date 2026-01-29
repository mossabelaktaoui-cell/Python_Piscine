import math
import sys


def create_position() -> None:
    print("=== Game Coordinate System ===\n")

    list_args = []

    for arg in sys.argv[1:]:
        list_args += arg.split(',')

    if len(list_args) == 1:
        original = list_args[0]
        list_args = list_args[0].split(', ')
        print(f"Parsing coordinates: \"{original}\"")
    if len(list_args) == 0:
        print("No arguments provided.")
        return
    elif len(list_args) <= 2:
        print("Error: Not enough arguments provided.")
        return
    elif len(list_args) > 3:
        print("Error: Too many arguments provided.")
        return

    try:
        for i in range(len(list_args)):
            coordinate = list_args[i]
            list_args[i] = int(list_args[i])

    except ValueError as e:
        print(f"Parsing Invalid Coordinates: \"{coordinate}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")
        return

    position = tuple(list_args)
    x, y, z = position
    distance = math.sqrt(x**2 + y**2 + z**2)

    print(f"Parsed position: {position}")
    print(f"Distance between (0, 0, 0) and {position}: {distance:.2f}")

    print("\nUnpacking demonstration")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    create_position()
