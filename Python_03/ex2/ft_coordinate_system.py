import math
import sys


def create_position():
    """
    Parses coordinates from sys.argv and calculates 3D Euclidean distance.
    Handles both separate arguments and comma-separated strings.
    """
    if len(sys.argv) < 2:
        print("No coordinates provided.")
        return
    list_args = []
    for arg in sys.argv[1:]:
        list_args.append(arg)
    try:
        position = (int(list_args[0]), int(list_args[1]), int(list_args[2]))
        print(f"Position created: {position}")
        x, y, z = position
        distance = math.sqrt(x**2 + y**2 + z**2)
        print(f"Distance between (0, 0, 0) and {position}: {distance:.2f}")
    except ValueError:
        if len(list_args) == 1:
            coordinates = list_args[0].split(',')
        else:
            coordinates = list_args
        i = 0
        while i < len(coordinates):
            try:
                coordinates[i] = int(coordinates[i])
            except ValueError as e:
                print(f"Error parsing coordinates: {e}")
                print(f"Error details - Type: ValueError, Args: (\"{e}\",)")
                return
            i += 1
        print(f"Parsing coordinates: \"{list_args[0]}\"")
        coordinates = tuple(coordinates)
        print(f"Parsed position: {coordinates}")
        x, y, z = coordinates
        distance = math.sqrt(x**2 + y**2 + z**2)
        print(f"Distance between (0, 0, 0) and {coordinates}: {distance:.2f}")
    print("\nUnpacking demonstration")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    create_position()