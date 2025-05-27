x = int(input ("Enter the first number: "))
y = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")
if y == 0:
 print("Cannot divide by zero.")
match operation:
    case "+":
        print ("The result is " + str (x + y) + ".")
    case "-":
        print(" The result is "+ str(x-y) + ".")
    case "*":
        print("The result is " + str (x*y) + ".")
    case "/": 
        print("The result is " + str(x/y) + ".")
    case _:
        print("wrong operator used")