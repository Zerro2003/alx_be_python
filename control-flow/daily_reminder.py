# Prompt for a Single Task
task = input('Enter your task: ')
priority = input('Priority (high/medium/low)?: ')
time_bound = input('Is it time-bound (yes/no)?: ')

# Process the Task Based on Priority
match priority.lower():  # Convert input to lowercase to handle case-insensitivity
    case 'high':
        print('Your task is high priority.')
    case 'medium':
        print('Your task is medium priority.')
    case 'low':
        print('Your task is low priority.')
    case _:
        print('Unknown priority.')

# Modify the output if the task is time-bound
if time_bound.lower() == 'yes':
    print(f'Reminder: {task} is a high priority task that requires immediate attention today!')
else:
    print(f'Note: {task} is a task to consider completing when you have free time.')
