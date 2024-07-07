def main():
    """Prompts user for task details, determines priority and time sensitivity, and displays a reminder."""

    task = input("Enter a task description: ")
    priority = input("Enter the task's priority (high, medium, low): ").lower()
    time_bound = input("Is this a time-bound task (yes or no)?: ").lower()

    # Match case for priority levels
    match priority:
        case "high":
            reminder_prefix = "**HIGH PRIORITY:** Don't forget to "
        case "medium":
            reminder_prefix = "**MEDIUM PRIORITY:** You should "
        case "low":
            reminder_prefix = "**LOW PRIORITY:** It would be good to "
        case _:
            reminder_prefix = "**Task:** "  # Default case for invalid priority

    # Modify reminder based on time sensitivity
    if time_bound == "yes":
        print(f" reminder: **{task}** that requires immediate attention today!")
    else:
        reminder_prefix += f"{task}."

    print(reminder_prefix)


if __name__ == "__main__":
    main()
