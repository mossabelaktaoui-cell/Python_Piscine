def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        file = open("ancient_fragment.txt", 'r')
        print("Connection established...")

        print("\nRECOVERED DATA:")
        print(file.read())

        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("Error: Storage Vault not found. Data recovery failed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
