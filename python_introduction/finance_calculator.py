income= int(input("Enter your monthly income: "))
expenses= int(input("Enter your total monthly expenses: "))
saving=income-expenses
projectedSavings = int(saving * 12 + (saving * 12 * 0.05))
print("Your monthly savings are $"+str(saving))
print("Projected savings after one year, with interest, is: $"+str(projectedSavings)+".")