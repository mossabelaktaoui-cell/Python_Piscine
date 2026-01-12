import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

id = input("Input Stream active. Enter archivist ID: ")
status = input("Input Stream active. Enter status report: ")
print()

print("{[}STANDARD{]}"f" Archive status from {id}: {status}")
print("{[}ALERT{]} System diagnostic: Communication channels verified", file=sys.stderr)
print("{[}STANDARD{]} Data transmission complete")

print("\nThree-channel communication test successful.")
