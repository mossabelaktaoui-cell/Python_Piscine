print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

with open("classified_data.txt", 'a+') as file:
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    
    print("\nSECURE EXTRACTION:")
    file.seek(0)
    print(file.read())

    print("\nSECURE PRESERVATION:")
    file.write("\n{[}CLASSIFIED{]} New security protocols archived")
    print("{[}CLASSIFIED{]} New security protocols archived")
    print("Vault automatically sealed upon completion")

print("\nAll vault operations completed with maximum security.")
