"""
Easter is celebrated on the Sunday immediately after the first full moon following the
spring equinox. Because its date includes a lunar component, Easter does not have
a fixed date in the Gregorian calendar. Instead, it can occur on any date between
March 22 and April 25. The month and day for Easter can be computed for a given
year using the Anonymous Gregorian Computus algorithm, which is shown below.

Set a equal to the remainder when year is divided by 19
Set b equal to the floor of year divided by 100
Set c equal to the remainder when year is divided by 100
Set d equal to the floor of b divided by 4
Set e equal to the remainder when b is divided by 4
Set f equal to the floor of (b + 8) divided by 25
Set g equal to the floor of (b − f + 1) divided by 3
Set h equal to the remainder when 19a + b − d − g + 15 is divided by 30
Set i equal to the floor of c divided by 4
Set k equal to the remainder when c is divided by 4
Set l equal to the remainder when 32 + 2e + 2i − h − k is divided by 7
Set m equal to the floor of (a + 11h + 22l) divided by 451
Set month equal to the floor of (h + l − 7m + 114) divided by 31
Set day equal to one plus the remainder when (h + l − 7m + 114) is divided by 31

Write a program that implements the Anonymous Gregorian Computus algorithm
to compute the date of Easter. Your program should read the year from the user and
then display an appropriate message that includes the date of Easter in that year.
"""

# Read the year from the user
year = int(input("Enter a year: "))

# Apply the Anonymous Gregorian Computus algorithm
a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451
month = (h + l - 7 * m + 114) // 31
day = 1 + (h + l - 7 * m + 114) % 31

# Display the result
print(f"Easter in the year {year} falls on {month}/{day}")
