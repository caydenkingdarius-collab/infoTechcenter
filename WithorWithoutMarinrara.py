#Main Branch

#betatestdev

# ============================================
# Welcome Branch
# Developer: Cayden Johnson
# Program: InfoTechCenter OS Boot Screen
# Version: 1.0
# ============================================

# Import required standard libraries
import sys      # Used for writing output without a newline
import time     # Used for delays (sleep)
import os       # Used for operating system interactions

# Enable ANSI escape codes on Windows terminals
# This allows color codes to work properly
if os.name == "nt":
    os.system("")

# ANSI color codes for terminal styling
GREEN = "\033[92m"      # Green text color
BLACK_BG = "\033[40m"   # Black background color
RESET = "\033[0m"       # Reset colors back to default

# Clear screen styling and apply colors
print(BLACK_BG + GREEN, end="")

# Display welcome messages
print("\nWelcome Branch - Developer: Cayden Johnson")
print("\nWelcome to infotech center V.1.0")

# Initialize counters
x = 0           # Controls how long the boot loop runs
ellipsis = 0    # Controls the number of dots in the loading animation

# Boot-up animation loop
while x != 20:
    x += 1

    # Create loading message with animated dots
    ellipsisMessage = "InfoTechCenter OS Booting" + "." * ellipsis
    ellipsis += 1

    # Overwrite the same line in the terminal
    sys.stdout.write("\r" + ellipsisMessage + "   ")
    sys.stdout.flush()

    # Pause to create animation effect
    time.sleep(0.5)

    # Reset dots after reaching three
    if ellipsis == 4:
        ellipsis = 0

    # Final boot message when loop completes
    if x == 20:
        print("\nOperating system Booted up - Retina scammed - Access Granted")

# Reset terminal colors before exiting
print(RESET)

# Weather Branch
# This program adjusts an alarm time and recommends a safe driving speed
# based on current weather conditions.

from datetime import datetime, timedelta


# ---------------------------------------------------
# Function: adjust_alarm
# Purpose:
#   Adjusts the alarm time earlier if weather conditions
#   could cause slower or more dangerous travel.
#
# Parameters:
#   original_alarm_time (datetime): The user's normal alarm time
#   weather (str): Current weather condition
#
# Returns:
#   datetime: Updated alarm time (earlier if weather is bad)
# ---------------------------------------------------
def adjust_alarm(original_alarm_time, weather):

    # List of weather conditions that may slow down commuting
    # and therefore require waking up earlier
    bad_weather = ["Rainy", "Foggy", "Snowy", "Stormy", "Icy"]

    # Number of minutes to wake up earlier when weather is bad
    early_wakeup_minutes = 30

    # Check if the current weather is in the list of bad conditions
    if weather in bad_weather:
        # Subtract 30 minutes from the original alarm time
        # timedelta is used to safely handle time arithmetic
        return original_alarm_time - timedelta(minutes=early_wakeup_minutes)
    else:
        # If the weather is good, keep the original alarm time
        return original_alarm_time


# ---------------------------------------------------
# Function: recommended_speed
# Purpose:
#   Determines a safe driving speed based on weather conditions.
#
# Parameters:
#   weather (str): Current weather condition
#
# Returns:
#   int: Recommended speed in miles per hour (mph)
# ---------------------------------------------------
def recommended_speed(weather):

    # Dictionary that maps weather conditions to safe driving speeds
    # Speeds are lower for dangerous conditions like ice or snow
    weather_speed_limits = {
        "Sunny": 70,
        "Cloudy": 65,
        "Rainy": 55,
        "Foggy": 45,
        "Snowy": 35,
        "Stormy": 30,
        "Icy": 25
    }

    # Return the speed associated with the weather condition
    # If the weather is not found in the dictionary,
    # default to 50 mph as a safe fallback
    return weather_speed_limits.get(weather, 50)


# ---------------------------------------------------
# Main Program Execution
# This block only runs when the script is executed directly
# ---------------------------------------------------
if __name__ == "__main__":

    # Set the normal alarm time to 7:00 AM
    # datetime.strptime converts a string into a datetime object
    alarm_time = datetime.strptime("07:00", "%H:%M")

    # Define the current weather condition
    current_weather = "Snowy"

    # Adjust the alarm time based on weather conditions
    updated_alarm = adjust_alarm(alarm_time, current_weather)

    # Get a safe driving speed recommendation
    safe_speed = recommended_speed(current_weather)

    # Display the results to the user
    print(f"Weather: {current_weather}")
    print(f"Original alarm: {alarm_time.strftime('%I:%M %p')}")
    print(f"Updated alarm: {updated_alarm.strftime('%I:%M %p')}")
    print(f"Recommended driving speed: {safe_speed} mph")


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
    if has_snacks or has_slurpies:
        print("😋 Bonus: Treat yourself while you're there.")
    else:
        print("😐 Fuel only. No fun snacks this time.")
else:
    print("🚗 You're good to keep driving. No refuel needed right now.")



