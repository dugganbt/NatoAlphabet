import pandas as pd

"""
Author: Brian Duggan
This code is an exercise on dictionary and list comprehension. It asks the user to enter a word and responds with a
list of NATO alphabet words to phonetically spell the word. 

Credits to: Dr. Angela, 100 Days of Code: The Complete Python Pro Bootcamp
"""

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Import NATO alphabet
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

# dictionary comprehension to create a NATO alphabet dictionary
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# print(nato_dict) # checking the nato dictionary

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Ask user for a word
word = input("Enter a word: ")

# Generate a list of letters in the word
letter_list = [letter for letter in word]


# Function to get a NATO alphabet
def get_NATO_word(letter):
    return nato_dict.get(letter.upper())


# Generate a corresponding NATO alphabet
nato_list = [get_NATO_word(letter) for letter in letter_list]

# Respond with NATO alphabet list
print(nato_list)
