'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''
from fpdf import FPDF

# Create a PDF class instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# Set font for the title
pdf.set_font("Arial", size=16, style='B')

# Title
pdf.cell(200, 10, txt="Report", ln=True, align='C')

# Set font for the body
pdf.set_font("Arial", size=12)

# Add some text
text = """
This is a basic report generated using Python.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla facilisi. Integer nec velit nec turpis condimentum consequat.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
"""
pdf.multi_cell(0, 10, txt=text)

# Output the PDF to a file
pdf.output("report.pdf")
