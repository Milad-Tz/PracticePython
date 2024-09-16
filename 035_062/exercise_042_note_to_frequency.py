"""
The following table lists an octave of music notes, beginning with middle C, along with their frequencies:

    Note        Frequency (Hz)
    C4          261.63
    D4          293.66
    E4          329.63
    F4          349.23
    G4          392.00
    A4          440.00
    B4          493.88

Write a program that reads the name of a note from the user and displays the note’s frequency. The program should also
support notes from C0 to C8 by utilizing the relationship between octaves: the frequency of any note in octave `n` is half
the frequency of the corresponding note in octave `n + 1`.
"""

# Read the note from the user
note = input("Enter the note (e.g., C4, A4, G3): ")

# Extract the letter part and octave part
letter = note[0].upper()  # Note letter (C, D, E, F, G, A, B)
octave = int(note[1])  # Octave number (0 to 8)

# Base frequencies for notes in the 4th octave
if letter == 'C':
    base_frequency = 261.63
elif letter == 'D':
    base_frequency = 293.66
elif letter == 'E':
    base_frequency = 329.63
elif letter == 'F':
    base_frequency = 349.23
elif letter == 'G':
    base_frequency = 392.00
elif letter == 'A':
    base_frequency = 440.00
elif letter == 'B':
    base_frequency = 493.88
else:
    base_frequency = None

# Check if the note is valid and compute the frequency for the entered octave
if base_frequency is not None:
    # Adjust the frequency based on the octave
    frequency = base_frequency * (2 ** (octave - 4))

    # Display the frequency
    print(f"The frequency of {note} is {frequency:.2f} Hz.")
else:
    print("Invalid note entered.")
