FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(celsius, "°C")  

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(fahrenheit, "°F")  

temperature = float(input("Enter the temperature to convert:"))
option = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if option == "c":
    convert_to_fahrenheit(temperature)  
elif option == "f":
    convert_to_celsius(temperature) 
else:
    print("Invalid temperature. Please enter a numeric value.")

