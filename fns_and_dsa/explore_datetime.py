from datetime import datetime,timedelta

def display_current_datetime():    
    current_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)

display_current_datetime()

def calculate_future_date(num):
    future_date=datetime.now() + timedelta(days=num)
    return future_date.strftime("%Y-%m-%d")


num=int(input("Enter the number of days to add to the current date: "))
input("future date: "+calculate_future_date(num))
