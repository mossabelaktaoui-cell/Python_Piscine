print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

file = open("new_discovery.txt", 'w')
print("Initializing new storage unit: new_discovery.txt")
print("Storage unit created successfully...")

print("\nInscribing preservation data...")
file.write("[ENTRY 001] New quantum algorithm discovered\n")
file.write("[ENTRY 002] Efficiency increased by 347%\n")
file.write("[ENTRY 003] Archived by Data Archivist trainee\n")

file.close()

file = open("new_discovery.txt", 'r')
print(file.read())

print("\nData inscription complete. Storage unit sealed.")
print("Archive 'new_discovery.txt' ready for long-term preservation.")

file.close()
