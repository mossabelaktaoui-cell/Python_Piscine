import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    try:
        archivist_id = input("Input Stream active. Enter archivist ID: ")
        status = input("Input Stream active. Enter status report: ")
        print()

        print("[STANDARD]"f" Archive status from {archivist_id}: {status}")
        print("[ALERT] System diagnostic: Communication channels verified",
              file=sys.stderr)
        print("[STANDARD] Data transmission complete")

        print("\nThree-channel communication test successful.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
