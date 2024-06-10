'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: elderberry

print(fruits[:3])  # Output: ['apple', 'banana', 'cherry']
print(fruits[-2:]) # Output: ['date', 'elderberry']

fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']
