#Weather Branch

# Function that determines the maximum allowed speed based on weather
def speed_limiter(current_weather, desired_speed):
    # Dictionary that maps weather conditions to max safe speeds (mph)
    weather_speed_limits = {
        "Sunny": 70,
        "Cloudy": 65,
        "Rainy": 55,
        "Foggy": 45,
        "Snowy": 35,
        "Stormy": 30,
        "Icy": 25
    }

    # Get the max speed for the current weather
    # If the weather is unknown, default to 50 mph
    max_safe_speed = weather_speed_limits.get(current_weather, 50)

    # If the desired speed is higher than what is safe,
    # limit the speed to the max safe speed
    if desired_speed > max_safe_speed:
        return max_safe_speed
    else:
        return desired_speed


# Example usage of the function
if __name__ == "__main__":
    weather = "Snowy"        # Current weather condition
    driver_speed = 60        # Speed the driver wants to go

    # Calculate the safe speed based on weather
    safe_speed = speed_limiter(weather, driver_speed)

    # Output the result
    print(f"Weather: {weather}")
    print(f"Requested speed: {driver_speed} mph")
    print(f"Allowed speed: {safe_speed} mph")