task=input("Enter your task: ")
priority=input("Priority (high/medium/low): ")
time_bound=input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound=="yes":
            print("Reminder: '"+task+"' is a "+priority+"task that requires immediate attention today!")
        else:
             print("Note: '"+task+"' is a "+priority+"task. Consider completing it when you have free time.")
