num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("Choose the operation (+, -, *, /):")
match operation:
    case '+':
        input("The result is :"+str(num1+num2))
    case '-':
        input("The result is :"+str(num1-num2))
    case '*':
        input("The result is :"+str(num1*num2))
    case '/':
        if(num2==0):
            input("Cannot divide by zero.")
        else:
            input("The result is :"+str(num1/num2))
