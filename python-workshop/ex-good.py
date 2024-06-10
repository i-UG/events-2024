'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

import datetime

def get_time_of_day():
    now = datetime.datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    else:
        return "evening"

def main():
    user_name = input("Enter your name: ")
    time_of_day = get_time_of_day()

    greeting = f"Good {time_of_day}, {user_name}!"
    print(greeting)

if __name__ == "__main__":
    main()