FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(celsius, "°C")  

def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    print(fahrenheit, "°F")  

temperature = float(input("Enter a temperature you want to convert: "))
option = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
if option == "c":
    convert_to_fahrenheit(temperature)  
elif option == "f":
    convert_to_celsius(temperature) 
else:
    print("Please input 'C' or 'F'")


