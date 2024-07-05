task = input('Enter your task:')
priority = input('Priority(high/medium/low)?:')
time_bound = input('Is it time-bound(yes/no)')
match priority:
    case 'high':
        print('your task is high')
    case 'medium':
        print('your task is medium')
    case 'low':
        print('your task is low')
    case _: 
        print('anknown task')
if time_bound == 'yes':
    print('Reminder: ',task,' is a high priority task that requires immediate attention today!')
else:
    print('Note: ',task,' is a low priority task. Consider completing it when you have free time.')