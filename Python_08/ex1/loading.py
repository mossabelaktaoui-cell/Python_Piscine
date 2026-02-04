import sys

print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")

installed_libraries = 0

try:
    import pandas
    import numpy as np
    version = pandas.__version__
    print(f"[OK] pandas ({version}) - Data manipulation ready")
    installed_libraries += 1
except ImportError:
    print("[ERROR] pandas not installed")

try:
    import requests
    version = requests.__version__
    print(f"[OK] requests ({version}) - Network access ready")
    installed_libraries += 1
except ImportError:
    print("[ERROR] requests not installed")

try:
    import matplotlib
    from matplotlib import pyplot as plt
    version = matplotlib.__version__
    print(f"[OK] matplotlib ({version}) - Visualization ready")
    installed_libraries += 1
except ImportError:
    print("[ERROR] matplotlib not installed")


if installed_libraries != 3:
    sys.exit(1)


print("\nAnalyzing Matrix data...")
print("Processing 7 data points...")

temperature = np.random.randint(12, 25, size=7)
humidity = np.random.randint(5, 10, size=7)
days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

print("Generating visualization...")
plt.plot(days, temperature, marker='o', linestyle='-',
         linewidth=1, color='red', label='Temperature')
plt.plot(days, humidity, marker='o', linestyle='-',
         linewidth=1, color='blue', label='Humidity')

plt.title("Temperature/Humidity throughout the last week")
plt.ylabel("°C / %RH")

plt.grid(0.1)
plt.legend()

image_name = "matrix_analysis.png"
plt.savefig(image_name)

print("\nAnalysis complete!")
print(f"Results saved to: {image_name}")
