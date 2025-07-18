# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Match Case for priority level
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level."

# If the task is time-bound, modify the reminder
if time_bound == "yes":
    reminder += " That requires immediate attention today!"

# Print the customized reminder
print(reminder)
