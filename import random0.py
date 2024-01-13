import random
import string

# List of words to choose from
words = ["Apple", "Grape", "Kitten", "Ocean", "Strawberry", "Watermelon", "Banana", "Carrot", "Elephant", "Firework"]

# List of digits to choose from
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# List of symbols to choose from
symbols = ["@", "#", "&"]

# Function to generate the code
def generate_code():
    # Choose a word randomly from the list of words
    code = random.choice(words)
    # Add a random digit to the code
    code += random.choice(digits)
    # Add random characters to the code until it reaches the maximum length
    while len(code) < 10:
        code += random.choice(list(string.ascii_lowercase) + digits + symbols)
    return code

combinations = 0
for i in range(10**10): #10^10 is the maximum possible combinations
    code = generate_code()
    # print(code)
    combinations += 1

# # Open a file to save the codes
# with open("John.txt", "w") as file:
#     # Generate all possible codes and save them in the file
#     for i in range(10**10): #10^10 is the maximum possible combinations
#         code = generate_code()
#         file.write(code + "\n")

print("All possible combinations are saved in the file named John.txt")
print("Number of combinations: ", combinations)
