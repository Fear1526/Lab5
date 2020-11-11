# Imports random
import random

# sets a variable to be a random number from 1 to 100
rand_num = random.randrange(1,101)

# Asks the user to guess a number
user_answer = int(input("Guess a number:"))

# Creates counter variable
counter = 1
# While the user's answer was not correct it will go to the if statements inside
while user_answer != rand_num:
    # If the answer was lower it will display the answer is too low
    if user_answer < rand_num:
        print ("Answer is too low")
        # Gives the user another try
        user_answer = int(input("Guess a number:"))
        #adds 1 to counter
        counter = counter+1
     # If the answer was higher it will display the answer is too high
    if user_answer > rand_num:
         print ("Answer is too high")
         # Gives the user another try
         user_asnwer = int(input("Guess a number:"))
         #adds 1 to counter
         counter = counter+1

print(user_answer, "was correct! This took you", counter, "attempts.")


