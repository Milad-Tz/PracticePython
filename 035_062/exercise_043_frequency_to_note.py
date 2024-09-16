"""
This program reads a frequency from the user and checks if it corresponds to a known musical note
within a margin of error of 1 Hz for notes in the 4th octave. The program supports C4, D4, E4, F4, G4, A4, and B4.
"""

# Constants for note frequencies (in Hz)
C_NOTE_FREQ = 261.63
D_NOTE_FREQ = 293.66
E_NOTE_FREQ = 329.63
F_NOTE_FREQ = 349.23
G_NOTE_FREQ = 392.00
A_NOTE_FREQ = 440.00
B_NOTE_FREQ = 493.88

# Tolerance for matching a frequency to a note
ERROR_MARGIN = 1.0

# Reading the frequency input from the user
input_freq = float(input("Enter a frequency in Hz: "))

# Determine the musical note based on the input frequency
if C_NOTE_FREQ - ERROR_MARGIN <= input_freq <= C_NOTE_FREQ + ERROR_MARGIN:
    matched_note = "C4"
elif D_NOTE_FREQ - ERROR_MARGIN <= input_freq <= D_NOTE_FREQ + ERROR_MARGIN:
    matched_note = "D4"
elif E_NOTE_FREQ - ERROR_MARGIN <= input_freq <= E_NOTE_FREQ + ERROR_MARGIN:
    matched_note = "E4"
elif F_NOTE_FREQ - ERROR_MARGIN <= input_freq <= F_NOTE_FREQ + ERROR_MARGIN:
    matched_note = "F4"
elif G_NOTE_FREQ - ERROR_MARGIN <= input_freq <= G_NOTE_FREQ + ERROR_MARGIN:
    matched_note = "G4"
elif A_NOTE_FREQ - ERROR_MARGIN <= input_freq <= A_NOTE_FREQ + ERROR_MARGIN:
    matched_note = "A4"
elif B_NOTE_FREQ - ERROR_MARGIN <= input_freq <= B_NOTE_FREQ + ERROR_MARGIN:
    matched_note = "B4"
else:
    matched_note = ""

# Displaying the result based on the match
if matched_note == "":
    print("The frequency doesn't correspond to any known note.")
else:
    print(f"The frequency corresponds to the note {matched_note}.")
