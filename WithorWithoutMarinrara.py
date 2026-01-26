#Weather Branch

# Import the random module so we can generate random choices and numbers
import random

# Define a function called weather
def weather():
    # A list of possible weather conditions
    conditions = [
        "Sunny ☀️",
        "Cloudy ☁️",
        "Rainy 🌧️",
        "Stormy ⛈️",
        "Snowy ❄️",
        "Windy 🌬️",
        "Foggy 🌫️"
    ]
    
    # Generate a random temperature between -5 and 40 degrees Celsius
    temperature = random.randint(-5, 40)
    
    # Randomly choose one weather condition from the list
    condition = random.choice(conditions)
    
    # Return a formatted string describing the weather
    return f"Today's weather: {condition}, Temperature: {temperature}°C"

# This block checks if the file is being run directly
# (and not imported as a module in another file)
if __name__ == "__main__":
    # Call the weather function and print the result
    print(weather())