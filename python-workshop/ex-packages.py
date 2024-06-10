'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

# main_script.py

# Importing the text_processing package and its modules
from text_processing import string_operations, text_analysis

# Text to analyze
text = "Python is amazing!"

# Counting characters and words
num_characters = string_operations.count_characters(text)
num_words = string_operations.count_words(text)

# Analyzing sentiment
sentiment = text_analysis.analyze_sentiment(text)

# Print results
print("Number of characters:", num_characters)
print("Number of words:", num_words)
print("Sentiment analysis:", sentiment)
