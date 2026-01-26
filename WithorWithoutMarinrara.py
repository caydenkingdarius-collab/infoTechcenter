#Weather Branch

from datetime import datetime, timedelta

# Function to adjust alarm time based on weather conditions
def adjust_alarm(original_alarm_time, weather):
    # Weather conditions that require waking up earlier
    bad_weather = ["Rainy", "Foggy", "Snowy", "Stormy", "Icy"]

    # Minutes to wake up earlier if weather is bad
    early_wakeup_minutes = 30

    # Check if current weather is considered bad
    if weather in bad_weather:
        # Subtract time from the original alarm
        return original_alarm_time - timedelta(minutes=early_wakeup_minutes)
    else:
        # Keep the same alarm time if weather is good
        return original_alarm_time


# Function to determine safe driving speed based on weather
def recommended_speed(weather):
    # Dictionary mapping weather conditions to safe speeds (mph)
    weather_speed_limits = {
        "Sunny": 70,
        "Cloudy": 65,
        "Rainy": 55,
        "Foggy": 45,
        "Snowy": 35,
        "Stormy": 30,
        "Icy": 25
    }

    # Return the safe speed for the weather
    # If weather is unknown, default to 50 mph
    return weather_speed_limits.get(weather, 50)


# Main program
if __name__ == "__main__":
    # Set your normal alarm time (7:00 AM)
    alarm_time = datetime.strptime("07:00", "%H:%M")

    # Current weather condition
    current_weather = "Snowy"

    # Adjust alarm based on weather
    updated_alarm = adjust_alarm(alarm_time, current_weather)

    # Get recommended driving speed
    safe_speed = recommended_speed(current_weather)

    # Display results
    print(f"Weather: {current_weather}")
    print(f"Original alarm: {alarm_time.strftime('%I:%M %p')}")
    print(f"Updated alarm: {updated_alarm.strftime('%I:%M %p')}")
    print(f"Recommended driving speed: {safe_speed} mph")
