import random # Necessary for randomizing password.
import string # Necessary for grabbing different type of characters, see row 21-24.

def Shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList) # Put all the password characters together without spaces.

while True:
    try:
        password_length = int(input('Password length: '))

        if password_length <= 0:
            print('Input error, try again...')
            continue
    except ValueError:
        print('Input error, try again...')
        continue
    
    # Assign uppercase, lowercase, digits and special characters to variables.
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all to a single variable.
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Create the final password using random choices from the above combined variables.
    password = ''.join(random.choice(all_characters)
                    for _ in range(password_length))

    # Shuffle the password.
    password = Shuffle(password)

    # Print shuffled password.
    print(password)