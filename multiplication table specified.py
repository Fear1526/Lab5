# For loop to display the top row of multiplication table
for i in range (0,17,2):
    print(i if i != 0 else "x"," ", "\t", end="")
print("")

for i in range (11,0, -4):
    for j in range (0,18,2):
        print(i*j if j != 0 else i," ", "\t", end="")
    print("")