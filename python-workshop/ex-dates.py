'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

from datetime import datetime


def calculate_days_until_birthday(date_of_birth):

    # Convert date of birth string to datetime object
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d")

    # Get today's date
    today = datetime.now()

    # Get next birthday
    next_birthday = datetime(today.year, dob.month, dob.day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, dob.month, dob.day)

    # Calculate days until next birthday
    days_until_birthday = (next_birthday - today).days

    return days_until_birthday


print(calculate_days_until_birthday("2024-03-04"))  # Output: 292
