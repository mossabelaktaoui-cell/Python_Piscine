print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

try:
    open("lost_archive.txt", 'r')
except FileNotFoundError:
    print(f"\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")

try:
    open("classified_vault.txt", 'r')
except PermissionError:
    print(f"\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")

with open("standard_archive.txt", 'r'):
    print(f"\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    print("SUCCESS: Archive recovered - ``Knowledge preserved for humanity''")
    print("STATUS: Normal operations resumed")

print("\nAll crisis scenarios handled successfully. Archives secure.")
