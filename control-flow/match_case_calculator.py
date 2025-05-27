x = int(input ("Enter the first number: "))
y = int(input("Enter the second number: "))

Z = input(" Choose the operation (+, -, *, /):")
if y == 0:
 print("Cannot divide by zero.")
match Z:
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