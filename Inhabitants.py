# Surnames array
surname = ["McIntosh", "McGregor", "McDonald", "McKenzie"]

# Firstnames array
forename = ["Angus", "Hamish", "Morag", "Mhairi"]

# Array for all inhabitants
inhabitants = []

# Nested For loop to go through each name in surname and forename
for last in surname:
    for first in forename:
        # Creates a string of every firstname + surname and appends to array
        inhabitants.append(first + " " + last)

# Prints all names
print(inhabitants)



