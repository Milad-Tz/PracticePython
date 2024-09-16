"""
The following table lists the sound level in decibels for several common noises.
Noise Decibel Level:
    - Jackhammer: 130 dB
    - Gas Lawnmower: 106 dB
    - Alarm Clock: 70 dB
    - Quiet Room: 40 dB

Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table, the program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed, the program should display a message
indicating which noises the value is between. The program should also generate
reasonable output for values smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
"""

# Read the sound level in decibels from the user
decibel_level = int(input("Enter the sound level in decibels: "))

# Determine and display the corresponding noise or range
if decibel_level == 130:
    print("The noise level corresponds to a Jackhammer.")
elif decibel_level == 106:
    print("The noise level corresponds to a Gas Lawnmower.")
elif decibel_level == 70:
    print("The noise level corresponds to an Alarm Clock.")
elif decibel_level == 40:
    print("The noise level corresponds to a Quiet Room.")
elif decibel_level > 130:
    print("The noise level is greater than a Jackhammer.")
elif decibel_level < 40:
    print("The noise level is quieter than a Quiet Room.")
elif 106 < decibel_level < 130:
    print("The noise level is between a Gas Lawnmower and a Jackhammer.")
elif 70 < decibel_level < 106:
    print("The noise level is between an Alarm Clock and a Gas Lawnmower.")
elif 40 < decibel_level < 70:
    print("The noise level is between a Quiet Room and an Alarm Clock.")
