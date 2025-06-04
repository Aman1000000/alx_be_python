num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
def perform_operation():

 match operation:
  case "add":
    print (num1 + num2 )
  case "substract":
    print (num1 - num2 )
  case "multiply":
    print (num1 * num2 )
  case "divide":
    if num2 == 0:
      print ("can not divide by zero")
    else:
     print (num1 / num2 )
    

  case _:
        print("Invalid data type entered.")
perform_operation()
   
    
     