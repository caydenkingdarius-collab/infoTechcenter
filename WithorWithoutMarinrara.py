#Gasoline Branch

import random

# ------------------------------------------------------------
# CONFIGURATION SECTION
# ------------------------------------------------------------

# Total capacity of the gas tank (in gallons)
# This is used only for reference and clarity
TANK_CAPACITY = 16.0

# Quarter tank threshold (25% of total capacity)
QUARTER_TANK_LEVEL = TANK_CAPACITY * 0.25

# List of possible gas stations to randomly choose from
GAS_STATIONS = [
    "QuickFuel",
    "Pump N Go",
    "Rocket Gas",
    "Fuel Barn",
    "Speedway Plus",
    "EZ Stop",
    "Highway Fuel Hub",
    "Corner Gas"
]

# ------------------------------------------------------------
# INPUT SECTION
# ------------------------------------------------------------

# Ask the user for the current gas level
# This simulates reading the gas gauge

current_gas = round(random.uniform(0, 16.0), 2)


# ------------------------------------------------------------
# GAS LEVEL ANALYSIS
# ------------------------------------------------------------

print("\n--- Gas Level Analysis ---")

# Check if the gas level is below a quarter tank
if current_gas < QUARTER_TANK_LEVEL:
    print("⚠️ Gas level is below a quarter tank.")
    needs_refueling = True
else:
    print("✅ Gas level is sufficient.")
    needs_refueling = False

# ------------------------------------------------------------
# PHONE ALARM DECISION (SIMULATED)
# ------------------------------------------------------------

# Since Python cannot actually set a phone alarm,
# we simulate the logic and explain the decision.
if needs_refueling:
    print("⏰ Phone alarm should be set EARLIER to allow time for refueling.")
else:
    print("⏰ No need to change phone alarm.")

# ------------------------------------------------------------
# GAS STATION SELECTION
# ------------------------------------------------------------

print("\n--- Nearby Gas Stations ---")

# Randomly select between 3 and 5 gas stations from the list
available_stations = random.sample(GAS_STATIONS, random.randint(3, 5))

# Display the randomly selected gas stations
for station in available_stations:
    print(f"- {station}")

# ------------------------------------------------------------
# CHEAPEST GAS STATION DECISION
# ------------------------------------------------------------

# Randomly pick ONE station and declare it the cheapest
cheapest_station = random.choice(available_stations)

print(f"\n💰 Cheapest gas (probably): {cheapest_station}")

# ------------------------------------------------------------
# SNACKS AND SLURPIES CHECK
# ------------------------------------------------------------

# Randomly decide whether the cheapest station has snacks
has_snacks = random.choice([True, False])

# Randomly decide whether the cheapest station has Slurpies
has_slurpies = random.choice([True, False])

print("\n--- Important Amenities ---")

# Snacks availability result
if has_snacks:
    print("🍫 Snacks available: YES")
else:
    print("🍫 Snacks available: NO")

# Slurpies availability result
if has_slurpies:
    print("🥤 Slurpies available: YES")
else:
    print("🥤 Slurpies available: NO")

# ------------------------------------------------------------
# FINAL RECOMMENDATION
# ------------------------------------------------------------

print("\n--- Final Recommendation ---")

if needs_refueling:
    print(f"➡️ Stop at {cheapest_station} to refuel.")
    if has_snacks or has_slurpies:import random

# ------------------------------------------------------------
# CONFIGURATION SECTION
# ------------------------------------------------------------

# Total capacity of the gas tank (in gallons)
TANK_CAPACITY = 16.0

# Quarter tank threshold (25% of total capacity)
QUARTER_TANK_LEVEL = TANK_CAPACITY * 0.25

# List of possible gas stations
GAS_STATIONS = [
    "QuickFuel",
    "Pump N Go",
    "Rocket Gas",
    "Fuel Barn",
    "Speedway Plus",
    "EZ Stop",
    "Highway Fuel Hub",
    "Corner Gas"
]

# ------------------------------------------------------------
# SIMULATED GAS SENSOR
# ------------------------------------------------------------

# Simulate reading the gas level from the vehicle
# This randomly generates a gas level between empty and full
current_gas = round(random.uniform(0, TANK_CAPACITY), 2)

print(f"🚘 Current gas level: {current_gas} gallons")

# ------------------------------------------------------------
# GAS LEVEL ANALYSIS
# ------------------------------------------------------------

print("\n--- Gas Level Analysis ---")

# Determine if the gas level is below a quarter tank
if current_gas < QUARTER_TANK_LEVEL:
    print("⚠️ Gas level is below a quarter tank.")
    needs_refueling = True
else:
    print("✅ Gas level is sufficient.")
    needs_refueling = False

# ------------------------------------------------------------
# PHONE ALARM DECISION (SIMULATED)
# ------------------------------------------------------------

# Simulate adjusting the phone alarm
if needs_refueling:
    print("⏰ Phone alarm should be set EARLIER for a fuel stop.")
else:
    print("⏰ No alarm adjustment needed.")

# ------------------------------------------------------------
# GAS STATION SELECTION
# ------------------------------------------------------------

print("\n--- Nearby Gas Stations ---")

# Randomly choose 3–5 gas stations
available_stations = random.sample(GAS_STATIONS, random.randint(3, 5))

# Display them
for station in available_stations:
    print(f"- {station}")

# ------------------------------------------------------------
# CHEAPEST GAS STATION DECISION (ALSO VERY SCIENTIFIC)
# ------------------------------------------------------------

# Randomly select the "cheapest" station
cheapest_station = random.choice(available_stations)

print(f"\n💰 Cheapest gas (trust me): {cheapest_station}")

# ------------------------------------------------------------
# SNACKS AND SLURPIES CHECK
# ------------------------------------------------------------

# Randomly decide snack and Slurpie availability
has_snacks = random.choice([True, False])
has_slurpies = random.choice([True, False])

print("\n--- Important Amenities ---")

print(f"🍫 Snacks available: {'YES' if has_snacks else 'NO'}")
print(f"🥤 Slurpies available: {'YES' if has_slurpies else 'NO'}")

# ------------------------------------------------------------
# FINAL RECOMMENDATION
# ------------------------------------------------------------

print("\n--- Final Recommendation ---")

if needs_refueling:
    print(f"➡️ Stop at {cheapest_station} to refuel.")
    if has_snacks or has_slurpies:
        print("😋 Bonus: Happiness included.")
    else:
        print("😐 Fuel only. Emotional support unavailable.")
else:
    print("🚗 No refuel needed. Keep cruising.")
