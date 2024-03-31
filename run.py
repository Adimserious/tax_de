import datetime
x = datetime.datetime.now()
print(x)

avarage_circle = 28
avarage_length = 4

def calculate_ovulation():
    """period data input from user"""
    print("what was the first day of your last period?\n")
    last_period = input("enter last period: ")
    print(f"The date you entered is {last_period}")

    print("what is your avarage cycle length?\n")
    avarage_length = input("enter cycle length: ")
    print(f"The number you entered is {avarage_length}")
    

calculate_ovulation()