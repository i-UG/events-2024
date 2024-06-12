'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('employees.db')

# Create a cursor object to execute SQL queries
c = conn.cursor()

# Create a table named "employees"
c.execute('''CREATE TABLE IF NOT EXISTS employees (
             id INTEGER PRIMARY KEY,
             name TEXT,
             age INTEGER,
             position TEXT,
             salary REAL)''')

# Insert 20 records into the "employees" table
for i in range(1, 21):
    name = f"Employee {i}"
    age = 20 + i
    position = "Manager" if i % 2 == 0 else "Developer"
    salary = 50000 + (i * 1000)
    c.execute('''INSERT INTO employees (name, age, position, salary)
                 VALUES (?, ?, ?, ?)''', (name, age, position, salary))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database & table created successfully with 20 records.")
