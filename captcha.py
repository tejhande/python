import random
import string

def generate_captcha():
    # Generate random string as challenge
    challenge = "".join(random.choices(string.ascii_letters + string.digits, k=5))
    return "Are you human? Please type the following characters: " + challenge

# Get captcha and display it
captcha = generate_captcha()
print(captcha)

# Get user input
answer = input().strip()

# Check if answer is correct
if answer == captcha[-5:]:
    print("CAPTCHA verification successful.")
else:
    print("CAPTCHA verification failed.")
