import random
import string

def generate_password(length):
    # Generate random string of specified length
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return password

def is_strong_password(password):
    # Check password length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter
    has_uppercase = any(char.isupper() for char in password)
    if not has_uppercase:
        return False
    
    # Check for at least one lowercase letter
    has_lowercase = any(char.islower() for char in password)
    if not has_lowercase:
        return False
    
    # Check for at least one digit
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False
    
    # Check for at least one special character
    has_special = any(char in string.punctuation for char in password)
    if not has_special:
        return False
    
    return True

choice = input("Do you want the program to generate a strong password for you? (yes/no): ")
if choice.lower() == "yes":
    password = generate_password(16)
    if is_strong_password(password):
        print("Generated password:", password)
    else:
        print("Sorry, unable to generate a strong password.")
else:
    password = input("Enter a password: ")
    if is_strong_password(password):
        print("Password is strong.")
    else:
        print("Password is not strong. Please try again.")
