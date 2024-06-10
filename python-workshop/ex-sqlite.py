'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

import sqlite3

# Function to create the "students" table
def create_table():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 age INTEGER,
                 city TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into the "students" table
def insert_data(name, age, city):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''INSERT INTO students (name, age, city)
                 VALUES (?, ?, ?)''', (name, age, city))
    conn.commit()
    conn.close()

# Function to retrieve and print all rows from the "students" table
def print_all_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM students''')
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Create the "students" table
create_table()

# Insert data into the "students" table
insert_data('Alice', 20, 'London')
insert_data('Bob', 21, 'Glasgow')

# Retrieve and print all rows from the "students" table
print("All Students:")
print_all_students()
