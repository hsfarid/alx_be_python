import datetime

current_date = datetime.datetime.now()
def display_current_datetime():
    print(f"{current_date.year}-0{current_date.month}-0{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}")
display_current_datetime()

number_of_days = int(input("Enter number of days: "))
def calculate_future_date():
    tdelta = datetime.timedelta(days=number_of_days) 
    future_date = current_date + tdelta
    print(f"{future_date.year}-0{future_date.month}-0{future_date.day}")
calculate_future_date()