import datetime
from datetime import date

x = date.today()
print(x)

avarage_circle = 28
avarage_length = 4

def calculate_ovulation():
    """period data input from user"""

    print("what was the first day of your last period?")
    print("Data should be day, month and year, seperated by dots.")
    print("Example: 2024.04.02\n")

    last_period = input("enter last period: ")
    print(f"The date you entered is {last_period}")
    
    
    period_validation(last_period)

    print("what is your avarage cycle length?\n")
    circle_length = input("enter cycle length: ")
    print(f"The number you entered is {circle_length}")

    circle_validation(circle_length)
    

def period_validation(values):
    
    """"""
    try:
        if len(values) != 10:
            raise ValueError(
                f"values are required in form of year, month and day, you provided {len(values)}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


def circle_validation(value):
    """"""
    try:
        if len(value) != 1:
            raise ValueError(
                f"period length should be between 4 and 7, you provided {len(value)}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

calculate_ovulation()