import datetime
def display_current_datetime():
    """" Display the current date and time """
    current_date = datetime.now()
    formatted_time = current_date.strftime("%Y-%M-%D %H:%M:%S")
    # format: YYYY-MM-DD HH:MM:SS
    print(f"current date and time: {formatted_time}")

def calculate_future_date():
    """ Calculate and display a future date based on user input """
    display_current_datetime()   #show current date and time
    while True:
        days_to_add = int(input("Enter the number of days to add"))
        future_date = datetime.now() + timedelta(days = days_to_add)
        formatted_future_date = future_date.strftime("%Y-%M-d")
        #format:YYYY-MM-DD
        print(f"future_date: {formatted_future_date}")
