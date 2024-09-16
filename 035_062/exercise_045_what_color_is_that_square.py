"""
Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row, as shown below:
(book - page 34)

Write a program that reads a position from the user. Use an if statement to
determine if the column begins with a black square or a white square. Then use
modular arithmetic to report the color of the square in that row. For example, if the
user enters a1 then your program should report that the square is black. If the user
enters d5 then your program should report that the square is white. Your program
may assume that a valid position will always be entered. It does not need to perform
any error checking.
"""

# Read the position from the user
position = input("Enter a position (e.g., a1): ")

# Extract the column letter and row number from the position
column = position[0]
row = int(position[1])

# Determine the column number based on the letter
# 'a' corresponds to 1, 'b' to 2, and so on
if column == 'a':
    column_number = 1
elif column == 'b':
    column_number = 2
elif column == 'c':
    column_number = 3
elif column == 'd':
    column_number = 4
elif column == 'e':
    column_number = 5
elif column == 'f':
    column_number = 6
elif column == 'g':
    column_number = 7
elif column == 'h':
    column_number = 8

# Determine if the square is black or white
# A square is black if the sum of the column number and row number is even, and white if odd
if (column_number + row) % 2 == 0:
    print("The square is black.")
else:
    print("The square is white.")
