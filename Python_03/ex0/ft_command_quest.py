import sys


def ft_command_quest() -> None:
    args = sys.argv
    print("=== Command Quest ===")
    if len(args) <= 1:
        print("No arguments provided!")
    print(f"Program name: {args[0]}")
    if (len(args) > 1):
        print(f"Arguments received: {len(args) - 1}")
    i = 1
    while i < len(args):
        print(f"Argument {i}: {args[i]}")
        i += 1
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    ft_command_quest()
