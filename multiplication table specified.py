# For loop to display the top row of multiplication table 0 to 16 incrementing by 2
for i in range (0,17,2):
    # Displays the top row of table if i equals 0 it will display "x" else it will display numbers
    print(i if i != 0 else "x"," ", "\t", end="")
# Takes a new line every time nested for loop is complete
print("")

# For loop to display left side of table 11 to 3
for i in range (11,1, -4):
    # For loop to display multiplication table 0 to 16
    for j in range (0,17,2):
        # prints i*j if j doesnt equal 0 else prints i
        print(i*j if j != 0 else i," ", "\t", end="")
    # Takes a new line every time nested for loop is complete
    print("")