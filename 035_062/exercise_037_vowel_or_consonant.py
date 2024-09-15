"""
In this exercise, you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o, or u, then your program should display a message
indicating that the entered letter is a vowel. If the user enters y, then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise, your program should display a message indicating that the
letter is a consonant.
"""

# Prompt the user to enter a letter
letter = input("Enter a letter of the alphabet: ").lower()

# Check if the input is a single letter
if len(letter) != 1 or not letter.isalpha():
    print("Error: Please enter a single letter.")
else:
    # Check if the letter is a vowel, y, or a consonant
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    elif letter == 'y':
        print(f"{letter} is sometimes a vowel and sometimes a consonant.")
    else:
        print(f"{letter} is a consonant.")
