import datetime

current_date = datetime.datetime.now()
def display_current_datetime():
    print(f"Current date and time: {current_date.date()} {current_date.hour}:{current_date.minute}:{current_date.second}")
display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    delta_days = datetime.timedelta(days=number_of_days) 
    future_date = current_date + delta_days
    print(f"future date: {future_date.date()}")
calculate_future_date()