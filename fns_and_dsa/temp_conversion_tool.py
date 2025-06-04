def convert_to_celsius(fahrenheit):
    
    celsius = (5/9) * (fahrenheit - 32)
    print(celsius, "°C")  

def convert_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    print(fahrenheit, "°F")  

temperature = float(input("Enter a temperature you want to convert: "))
option = input("Type 'C' if it is Celsius and 'F' if it is Fahrenheit: ").lower()
if option == "c":
    convert_to_fahrenheit(temperature)  
elif option == "f":
    convert_to_celsius(temperature) 
else:
    print("Please input 'C' or 'F'")

