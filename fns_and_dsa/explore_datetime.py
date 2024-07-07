from datetime import datetime, timedelta

def display_current_datetime():
  """
  This function gets the current date and time and prints it in a readable format.
  """
  current_date = datetime.now()
  formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
  """
  This function prompts the user for the number of days and calculates the future date.
  """
  number_of_days = int(input("Enter the number of days to add to the current date: "))
  current_date = datetime.now()
  future_date = current_date + timedelta(days=number_of_days)
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  print(f"The date {number_of_days} days from now will be: {formatted_future_date}")

# Call the functions
display_current_datetime()
calculate_future_date()
