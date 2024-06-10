'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

def greet(name):
    """
    Prints a greeting message with the provided name.
    """
    print(f"Hello, {name}! Welcome to the Python script.")

if __name__ == "__main__":
    # Prompt the user to enter their name
    user_name = input("Please enter your name: ")
    # Call the greet function with the entered name
    greet(user_name)

