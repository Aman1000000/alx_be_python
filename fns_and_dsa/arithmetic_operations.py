num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
def perform_operation(num1, num2, operation):
 match operation:
  case "add":
   print (num1 + num2 )
  case "subtract":
   print (num1 - num2 )
  case "multiply":
   print (num1 * num2 )
  case "divide":
   if num2 != 0:
    print (num1 / num2 )
   elif num2 == 0 :
    print ("can not divide by zero")
  case _:
   print("Invalid data type entered.")
 return perform_operation
perform_operation(num1 ,num2 , operation) 
   
    
     