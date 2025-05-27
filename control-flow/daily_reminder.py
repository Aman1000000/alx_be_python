loop = False
while loop <= 100:
 task = input ( "Enter your task: " )
 priority = input ("Priority (high/medium/low): ")
 time = input ("Is it time-bound? (yes/no): ")
 match priority:
   case  meduim:
    medium = " "
   
 if time == "yes":
  loop = True
  print (f"{task} is a {priority} priority task, that requires immediate attention today! ")
 elif time == "no":
  print( (f"{task} is a {priority} priority task. Consider completing it when you have free time.") )
  
  