file = open("ancient_fragment.txt", 'r')

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
print("Accessing Storage Vault: ancient_fragment.txt")
print("Connection established...")
print("\nRECOVERED DATA:")

print(file.read())

print("\nData recovery complete. Storage unit disconnected.")

file.close()
