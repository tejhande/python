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

# Get the minimum and maximum length of the password from the user
min_length = int(6)
max_length = int(8)

# Generate a strong password of a random length within the given range
password_length = random.randint(min_length, max_length)
password = generate_password(password_length)

# Print the generated password
print("Your password is:", password)
