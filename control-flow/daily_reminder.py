task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"'{task}' is a high priority task", end="")
    case "medium":
        print(f"'{task}' is a medium priority task", end="")
    case "low":
        print(f"'{task}' is a low priority task", end="")
    case _:
        print("Invalid priority level.", end="")

if time_bound == "yes":
    print(" that requires immediate attention today!")
else:
    print()