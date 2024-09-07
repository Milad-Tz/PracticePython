"""
This program uses Python's time module to display the current time and date.
The asctime() function reads the current time from the computer's internal clock
and returns it in a human-readable format.
"""

import time

# Get the current time and date in a human-readable format
current_time = time.asctime()

# Display the current time and date
print("The current time and date is:", current_time)
