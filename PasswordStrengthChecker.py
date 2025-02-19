import re # Regular Expression Operations

# Password Validation Function
def password_validation(password):
    # Check if password contains 8 or more characters
    if len(password) < 8:
        return False
    # Check if password contains at least 1 uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    # Check if password contains at least 1 lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    # Check if password contains at least 1 digit
    if not re.search(r'\d', password):
        return False
    # Check if password contains at least 1 special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    # If password contains all of the above, password is valid
    return True

valid = False

# Program will loop until a valid password is entered
while not valid:
    password = input("Enter password: ")
    valid = password_validation(password)
    if valid:
        print("Password is valid.")
        break
    else:
        print("Password doesn't meet all requirements.")