# Prompt the user for task description
task = input("Please enter the task description: ")

# Prompt for the task's priority
priority = input("Enter the task's priority (high, medium, low): ").lower()

# Prompt to check if the task is time-bound
time_bound_input = input("Is this task time-bound? (yes/no): ").lower()
time_bound = True if time_bound_input == 'yes' else False

# Process based on priority using match-case
match priority:
    case 'high':
        priority_level = 'High'
    case 'medium':
        priority_level = 'Medium'
    case 'low':
        priority_level = 'Low'
    case _:
        priority_level = 'Unknown'

# Generate the reminder message
reminder = f"Reminder: '{task}' with {priority_level} priority."

# Modify the reminder if the task is time-bound
if time_bound:
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print(reminder)
