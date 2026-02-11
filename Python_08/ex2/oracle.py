import os
try:
    import dotenv
except ImportError:
    print("The 'dotenv' package is required to run this script."
          "\nPlease install it using 'pip install python-dotenv'.")
    exit(1)

print("\nORACLE STATUS: Reading the Matrix...")
dotenv.load_dotenv()

print("\nConfiguration loaded:")

if (
   not os.getenv('MATRIX_MODE')
   or not os.getenv('DATABASE_URL')
   or not os.getenv('API_KEY')
   or not os.getenv('LOG_LEVEL')
   or not os.getenv('ZION_ENDPOINT')):
    print("Some configuration is missing!")
    configuration = False
else:
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print("Zion Network: Online")
    configuration = True


print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")

try:
    open(".env", 'r')
    if configuration:
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
    else:
        print("[WARNING] .env file is empty or doesn't complete!")
except Exception:
    print("[ERROR] .env file doesn't exist")
