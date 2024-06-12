'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('employees.db')

# Query all records from the "employees" table
df = pd.read_sql_query("SELECT * FROM employees", conn)

# Export the DataFrame to an Excel spreadsheet
excel_file = "employees.xlsx"
df.to_excel(excel_file, index=False)

print(f"Data exported to {excel_file} successfully.")

# Close the connection
conn.close()