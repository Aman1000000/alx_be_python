from datetime import datetime, timedelta

def display_current_datetime():
    
    current_datetime = datetime.now()

    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)

def calculate_future_date(days_to_add):
    
    current_date = datetime.now().date()
    time_to_add = timedelta(days=days_to_add)
    future_date = current_date + time_to_add
    return future_date.strftime("%Y-%m-%d")

if __name__ == "__main__":

    display_current_datetime()
    days_input = input("Enter the number of days to add to the current date: ")

    if days_input.isdigit():
        days_input = int(days_input)
        future_date = calculate_future_date(days_input)
        print("Future date:", future_date)
    else:
        print("Please enter a valid integer.")

