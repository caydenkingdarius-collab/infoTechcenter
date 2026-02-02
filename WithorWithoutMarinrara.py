import random  # Used to generate random values for simulation

"""
Gas Monitoring System
---------------------
This program simulates a basic car gas monitoring system.

It performs the following steps:
1. Reads the car's current gas level (randomized)
2. Checks whether the gas level is below a safe threshold
3. Finds nearby gas stations
4. Determines the closest and cheapest station
5. Triggers an alert if the gas level is low

NOTE:
- All data is mocked (fake) for learning/testing purposes.
- Real-world versions would use car sensors, GPS, and external APIs.
"""

# -------------------------------
# CONFIGURATION
# -------------------------------

# Minimum safe gas level (percentage)
# If gas falls below or equals this value, the system triggers an alert
LOW_GAS_THRESHOLD = 25  

# Enables or disables the gas alert system
ALARM_ENABLED = True


# -------------------------------
# MOCK CAR DATA
# -------------------------------

def get_car_gas_level():
    """
    Simulates reading the car's current gas level.

    In a real system, this data might come from:
    - An OBD-II scanner
    - A connected vehicle API (Tesla, Ford, etc.)

    Returns:
        int: A random gas level between 0% and 100%
    """
    return random.randint(0, 100)


# -------------------------------
# MOCK LOCATION & GAS STATIONS
# -------------------------------

def get_current_location():
    """
    Simulates retrieving the car's GPS location.

    Returns:
        dict: Latitude and longitude of the car
    """
    return {"lat": 40.7128, "lon": -74.0060}  # Example location: New York City


def get_nearby_gas_stations(location):
    """
    Simulates finding nearby gas stations based on location.

    In a real application, this function might call:
    - Google Maps API
    - Yelp API
    - GasBuddy API

    Args:
        location (dict): The car's current GPS coordinates

    Returns:
        list: A list of gas stations with distance and fuel price
    """
    return [
        {"name": "Shell", "distance_km": 1.2, "price_per_gallon": 3.89},
        {"name": "Exxon", "distance_km": 0.8, "price_per_gallon": 3.99},
        {"name": "Costco Gas", "distance_km": 4.5, "price_per_gallon": 3.59},
    ]


# -------------------------------
# DECISION LOGIC
# -------------------------------

def needs_gas(gas_level):
    """
    Determines whether the car needs refueling.

    Args:
        gas_level (int): Current gas level percentage

    Returns:
        bool: True if gas is low, False otherwise
    """
    return gas_level <= LOW_GAS_THRESHOLD


def find_closest_gas_station(stations):
    """
    Finds the gas station with the shortest distance.

    Args:
        stations (list): List of gas station dictionaries

    Returns:
        dict: The closest gas station
    """
    return min(stations, key=lambda s: s["distance_km"])


def find_cheapest_gas_station(stations):
    """
    Finds the gas station with the lowest fuel price.

    Args:
        stations (list): List of gas station dictionaries

    Returns:
        dict: The cheapest gas station
    """
    return min(stations, key=lambda s: s["price_per_gallon"])


# -------------------------------
# ALERT SYSTEM
# -------------------------------

def trigger_gas_alarm(gas_level):
    """
    Displays a warning message when gas is critically low.

    Args:
        gas_level (int): Current gas level percentage
    """
    if ALARM_ENABLED:
        print("🚨 GAS ALERT 🚨")
        print(f"Gas level is LOW: {gas_level}%")
        print("Please refuel soon!")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

def main():
    """
    Main execution function.
    Controls the overall flow of the program.
    """

    # Get current gas level and location
    gas_level = get_car_gas_level()
    location = get_current_location()

    # Display current gas level
    print(f"Current gas level: {gas_level}%")

    # Check if refueling is required
    if needs_gas(gas_level):
        trigger_gas_alarm(gas_level)

        # Retrieve nearby gas stations
        stations = get_nearby_gas_stations(location)

        # Find best options
        closest = find_closest_gas_station(stations)
        cheapest = find_cheapest_gas_station(stations)

        # Display results
        print("\n⛽ Gas Stations:")
        print(f"Closest: {closest['name']} ({closest['distance_km']} km away)")
        print(f"Cheapest: {cheapest['name']} (${cheapest['price_per_gallon']}/gal)")
    else:
        print("✅ Gas level is sufficient. No need to refuel.")


# Program entry point
# Ensures the main function runs only when this file is executed directly
if __name__ == "__main__":
    main()
import random  # Used to generate random values for simulation

"""
Gas Monitoring System
---------------------
This program simulates a basic car gas monitoring system.

It performs the following steps:
1. Reads the car's current gas level (randomized)
2. Checks whether the gas level is below a safe threshold
3. Finds nearby gas stations
4. Determines the closest and cheapest station
5. Triggers an alert if the gas level is low

NOTE:
- All data is mocked (fake) for learning/testing purposes.
- Real-world versions would use car sensors, GPS, and external APIs.
"""

# -------------------------------
# CONFIGURATION
# -------------------------------

# Minimum safe gas level (percentage)
# If gas falls below or equals this value, the system triggers an alert
LOW_GAS_THRESHOLD = 25  

# Enables or disables the gas alert system
ALARM_ENABLED = True


# -------------------------------
# MOCK CAR DATA
# -------------------------------

def get_car_gas_level():
    """
    Simulates reading the car's current gas level.

    In a real system, this data might come from:
    - An OBD-II scanner
    - A connected vehicle API (Tesla, Ford, etc.)

    Returns:
        int: A random gas level between 0% and 100%
    """
    return random.randint(0, 100)


# -------------------------------
# MOCK LOCATION & GAS STATIONS
# -------------------------------

def get_current_location():
    """
    Simulates retrieving the car's GPS location.

    Returns:
        dict: Latitude and longitude of the car
    """
    return {"lat": 40.7128, "lon": -74.0060}  # Example location: New York City


def get_nearby_gas_stations(location):
    """
    Simulates finding nearby gas stations based on location.

    In a real application, this function might call:
    - Google Maps API
    - Yelp API
    - GasBuddy API

    Args:
        location (dict): The car's current GPS coordinates

    Returns:
        list: A list of gas stations with distance and fuel price
    """
    return [
        {"name": "Shell", "distance_km": 1.2, "price_per_gallon": 3.89},
        {"name": "Exxon", "distance_km": 0.8, "price_per_gallon": 3.99},
        {"name": "Costco Gas", "distance_km": 4.5, "price_per_gallon": 3.59},
    ]


# -------------------------------
# DECISION LOGIC
# -------------------------------

def needs_gas(gas_level):
    """
    Determines whether the car needs refueling.

    Args:
        gas_level (int): Current gas level percentage

    Returns:
        bool: True if gas is low, False otherwise
    """
    return gas_level <= LOW_GAS_THRESHOLD


def find_closest_gas_station(stations):
    """
    Finds the gas station with the shortest distance.

    Args:
        stations (list): List of gas station dictionaries

    Returns:
        dict: The closest gas station
    """
    return min(stations, key=lambda s: s["distance_km"])


def find_cheapest_gas_station(stations):
    """
    Finds the gas station with the lowest fuel price.

    Args:
        stations (list): List of gas station dictionaries

    Returns:
        dict: The cheapest gas station
    """
    return min(stations, key=lambda s: s["price_per_gallon"])


# -------------------------------
# ALERT SYSTEM
# -------------------------------

def trigger_gas_alarm(gas_level):
    """
    Displays a warning message when gas is critically low.

    Args:
        gas_level (int): Current gas level percentage
    """
    if ALARM_ENABLED:
        print("🚨 GAS ALERT 🚨")
        print(f"Gas level is LOW: {gas_level}%")
        print("Please refuel soon!")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

def main():
    """
    Main execution function.
    Controls the overall flow of the program.
    """

    # Get current gas level and location
    gas_level = get_car_gas_level()
    location = get_current_location()

    # Display current gas level
    print(f"Current gas level: {gas_level}%")

    # Check if refueling is required
    if needs_gas(gas_level):
        trigger_gas_alarm(gas_level)

        # Retrieve nearby gas stations
        stations = get_nearby_gas_stations(location)

        # Find best options
        closest = find_closest_gas_station(stations)
        cheapest = find_cheapest_gas_station(stations)

        # Display results
        print("\n⛽ Gas Stations:")
        print(f"Closest: {closest['name']} ({closest['distance_km']} km away)")
        print(f"Cheapest: {cheapest['name']} (${cheapest['price_per_gallon']}/gal)")
    else:
        print("✅ Gas level is sufficient. No need to refuel.")


# Program entry point
# Ensures the main function runs only when this file is executed directly
if __name__ == "__main__":
    main()
