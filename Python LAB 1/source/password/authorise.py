# Declaring the list of special symbols in a list
Spsymbols =['$','@','#','!']

while True:
    # Giving password as input
    password = input("Enter the password :")

    # Checking If the password length is less than 6 characters
    if len(password)< 6:
        print("Weak Password : Password Should contain atleast 6 characters ")
        continue
    # Checking if the password length is more than 16 characters
    elif len(password)> 16 :
        print("Length Exceeded: Password can have utmost of 16 characters ")
        continue
    # Check if the password has atleast one numeric character
    elif not any(char.isdigit() for char in password):
        print('Password should contain atleast one numeric character')
        continue
    # Checking if password has atleast one upper-case character:
    elif not any(char.isupper() for char in password):
        print('Password should contain at least one Upper-Case Character')
        continue
    # Checking if password has atleast one lower-case character:
    elif not any(char.islower() for char in password):
        print('the password should have at least one lowercase letter')
        continue
    # Checking if the password has atleast one special symbol
    elif not any(char in Spsymbols for char in password):
        print('Password should contain atleast one special symbol')
        continue
    else:
        print("The entered password meets all security requirements")
        print(password)
        break