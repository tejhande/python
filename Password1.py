# import string

# # Get all uppercase and lowercase letters, symbols and numbers
# alphabet = string.ascii_letters + string.punctuation + string.digits

# print(alphabet)

import random
import string

def generate_password(length):
    """
    Generate a strong password of a given length.
    """
    # Define the characters to be used in the password
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Shuffle the characters to make the password more random
    chars = random.sample(chars, len(chars))
    
    # Generate the password by randomly selecting characters from the shuffled list
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password

# Generate a strong password of length 12
password = generate_password(12)
print(password)

# import random

# # Prompt the user for minimum and maximum password length
# min_length = int(input("Enter minimum password length: "))
# max_length = int(input("Enter maximum password length: "))

# # Define the character sets
# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?~"

# # Generate all possible passwords within the specified length range
# passwords = []
# for length in range(min_length, max_length + 1):
#     for l in letters:
#         for n in numbers:
#             for s in special_chars:
#                 password = l + n + s
#                 if len(password) == length:
#                     passwords.append(password)
#                 password = l.upper() + n + s
#                 if len(password) == length:
#                     passwords.append(password)

# # Shuffle the passwords
# # random.shuffle(passwords)

# # Write the passwords to a file
# with open("passwords.txt", "w") as f:
#     for password in passwords:
#         f.write(password + "\n")
#         print(password + "\n")
# print("Passwords generated and saved to passwords.txt")
