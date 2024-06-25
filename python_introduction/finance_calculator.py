income = int(input('Enter your monthly income: '))
expenses = int(input('Enter your total monthly expenses: '))
monthly_savings = income - expenses
print('Your monthly savings are $', monthly_savings)
project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print('Projected savings after one year, with an interest, is: $', project_savings)
