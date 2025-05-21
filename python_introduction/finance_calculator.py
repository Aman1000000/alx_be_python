monthly_income = float (input ("Enter your monthly income: "))
monthly_expenses = float (input ("Enter your total monthly expense: "))
monthly_savings = monthly_income - monthly_expenses
monthly_savings = monthly_savings*12+(monthly_savings*12*0.05)
Result = "Enter your monthly income: " + str(monthly_income) + "\n" +"Enter your total monthly expense: " + str (monthly_expenses) + "\n" + "Your monthly savings are " + str (monthly_savings) +"\n" + "Projected savings after one year, with interest, is: " + str (monthly_savings)
print (Result)
