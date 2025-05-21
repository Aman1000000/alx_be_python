income = float (input ("Enter your monthly income: "))
expense = float (input ("Enter your total monthly expense: "))
saving = income - expense
Annual_saving = saving*12+(saving*12*0.05)
Result = "Enter your monthly income: " + str(income) + "\n" +"Enter your total monthly expense: " + str (expense) + "\n" + "Your monthly savings are " + str (saving) +"\n" + "Projected savings after one year, with interest, is: " + str (Annual_saving)
print (Result)
