monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your total monthly expenses: '))
monthly_savings = monthly_income - monthly_expenses
print (f'Your monthly savings are ${monthly_savings:.2f}')
project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print (f'Projected savings after one year, with an interest, is: ${project_savings:.2f}')
