'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

numbers = [1, 2, 3, 4, 5]
totalN = 0
totalW = 0
index = 0

for num in numbers:
    totalN += num

while index < len(numbers):
    totalW += numbers[index]
    index += 1

print(f"Sum using for loop: {totalN}")    # Output: 15
print(f"Sum using while loop: {totalW}")   # Output: 15

