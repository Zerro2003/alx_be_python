def daily_reminder():
    # Get task details from the user
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
    match priority:
        case "high":
            print(f"\n'{task}' is a high priority task", end="")
        case "medium":
            print(f"\n'{task}' is a medium priority task", end="")
        case "low":
            print(f"\n'{task}' is a low priority task", end="")
        case _:
            print(f"\n'{task}' is a task", end="")

    # Modify output based on time sensitivity
    if time_bound == "yes":
        print(" that requires immediate attention today!")
    else:
        if priority == "low":
            print(". Consider completing it when you have free time.")
        else:
            print(".")

# Run the daily reminder function
daily_reminder()