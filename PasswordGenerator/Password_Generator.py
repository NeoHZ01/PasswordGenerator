import random # Import random and string packages
import string
from unicodedata import digit

print("Hello welcome to password generator!") # A welcome message for the users using the password generator

# Declare the different data used for the password (uppercase, lowercase, number and symbol)

lower = string.ascii_lowercase # ascii lowercase is the lowercase alphabet of a string

upper = string.ascii_uppercase # ascii uppercase is the uppercase alphabet of a string

number = string.digits # digits is used for numbers

symbol = string.punctuation # punctuation is used for the different symbols

all = lower + upper + number + symbol # combine all the data 

checkLen = False # Bool to check whether the length of password is true or false

# While loop, if bool is false ask user for length of password
while not checkLen: 
    length = int(input('\nEnter the length of password: ')) # Check with user the length of password they want to generate

    # If password length is 8 or smaller, reject and explain why
    if (length) <= 8:
        print("Your password length is too short! (Must be more than 8 characters)")

    # If password length is more than 8, bool turn true
    elif (length) > 8:
        print("Your password length looks good!")
        checkLen = True
        
# While loop, if bool is true
while checkLen:
    # create a temporary variable with random module to generate the password
    # the random module will consist of the parameter which contain the combined data and the length of password 
    temp = random.sample(all, length)

    # as the generated password will be in the form of a list, combine the list using join method
    password = "".join(temp)
    print(password) 
    break

input("Press to exit") # to receive an input from the user to close the executable file
