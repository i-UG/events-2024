'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

import csv

# Student data
students = [
    {"id": 1, "name": "Alice", "age": 20, "job": "IT Director"},
    {"id": 2, "name": "Bob", "age": 21, "job": "Project Director"},
    {"id": 3, "name": "Charlie", "age": 22, "job": "Programming Language Manager"}
]

# CSV file path
csv_file = "students.csv"

# Write student data to CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ['id', 'name', 'age', 'job']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for student in students:
        writer.writerow(student)

print(f"CSV file '{csv_file}' has been created.")
