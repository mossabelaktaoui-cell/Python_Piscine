def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        with open("classified_data.txt", 'r+') as file:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols")

            print("\nSECURE EXTRACTION:")
            print(file.read())

            print("\nSECURE PRESERVATION:")
            file.write("\n[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except FileNotFoundError:
        print("Error: Vault access denied. Classified data not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
