def daily_reminder():
    # Get task details from the user
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' is a task"

    # Modify reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        if priority == "low":
            reminder = f"Note: {reminder}. Consider completing it when you have free time."
        else:
            reminder += "."

    # Print the customized reminder
    print("\n" + reminder)

# Run the daily reminder function
daily_reminder()