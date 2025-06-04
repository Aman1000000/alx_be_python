# Define conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the defined factor
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(celsius, "°C")  # Correct unit

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the defined factor
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    print(fahrenheit, "°F")  # Correct unit

# Get temperature input from user
temperature = float(input("Enter a temperature you want to convert: "))
option = input("Type 'C' if it is Celsius and 'F' if it is Fahrenheit: ").lower()

# Perform the conversion based on user input
if option == "c":
    convert_to_fahrenheit(temperature)  # Convert Celsius to Fahrenheit
elif option == "f":
    convert_to_celsius(temperature)  # Convert Fahrenheit to Celsius
else:
    print("Please input 'C' or 'F'")
