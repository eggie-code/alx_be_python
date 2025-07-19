# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Initialize reminder message
reminder_message = ""

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task."
    case _:
        reminder_message = f"'{task}' has an unspecified priority"

# Modify reminder if the task is time-bound
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder_message += " that requires immediate attention today!"
    else:
        reminder_message += " that you should aim to complete today."
elif time_bound == "no" and priority == "low":
    reminder_message += " Consider completing it when you have free time."
elif time_bound == "no":
    reminder_message += "."

# Provide a Customized Reminder
print(f"Reminder: {reminder_message}")
