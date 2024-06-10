'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

# ex-string-operations.py

def reverse_string(string):
    return string[::-1]

def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count
