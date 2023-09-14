import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    # As most of the platforms allow only these characters in password.
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the Desired length of the Password: "))

if(length<=0):
    print("Error: Invalid Input")
else:
    password = generate_password(length)
    print("Password:", password)