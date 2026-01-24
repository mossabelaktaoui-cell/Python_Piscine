import math
import sys


def create_position() -> None:
    list_args = []

    for arg in sys.argv[1:]:
        list_args += [arg]

    if len(list_args) == 0:
        print("No coordinates provided.")
        return
    if len(list_args) == 2:
        print("Error: Not enough coordinates provided.")
        return
    elif len(list_args) > 3:
        print("Error: Too many coordinates provided.")
        return

    try:
        if len(list_args) == 3:
            coordinates = None
            for i in range(len(list_args)):
                list_args[i] = int(list_args[i])

        elif len(list_args) == 1:
            coordinates = list_args[0]
            list_args = list_args[0].split(',')
            for i in range(len(list_args)):
                list_args[i] = int(list_args[i])
            print(f"Parsing coordinates: \"{coordinates}\"")

    except ValueError as e:
        if coordinates:
            print(f"Parsing Invalid Coordinates: \"{coordinates}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")
        return

    position = tuple(list_args)
    print(f"Parsed position: {position}")
    x, y, z = position
    distance = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance between (0, 0, 0) and {position}: {distance:.2f}")

    print("\nUnpacking demonstration")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    create_position()
