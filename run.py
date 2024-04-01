import datetime as dtt

from datetime import date

age = 60


def calculate_fertility():
    """Age data input from user"""

    print("how old are you?")
    print("Data should be number.")
    print("Example: 18\n")

    current_age = input("enter age: ")
    print(f"The number you entered is {current_age}")
    
    
    age_validation(current_age)

    print("are you married?")
    print("yes or no?.\n" )
    

    marital_status = input("enter status: ")
    
    print(f"you entered is {marital_status}")

    marriage_validation(marital_status)
    

def age_validation(values):
    
    """"""
    try:
        [int(valu) for valu in values]
        if len(values) != 2:
            raise ValueError(
                f"2 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


def marriage_validation(value):
    """"""

    try:
        if (value) != "Yes":    
            raise ValueError(
                f"Yes or No; you provided {value}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

calculate_fertility()