task = input("Enter a task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder = "This is a high priority task."
    case "medium":
        reminder = "This is a medium priority task."
    case "low":
        reminder = "This is a low priority task."
    case _:
        reminder = "Invalid priority level."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(f"Reminder: {task} - {reminder}")