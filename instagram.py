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
username_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "username")))
password_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "password")))
your_username = "dt1dt2d"
your_password = "Love@#Emiway"
# enter your username and password
username_input.send_keys(your_username)
password_input.send_keys(your_password)

# submit the form
password_input.send_keys(Keys.RETURN)

# wait for the popups to appear and dismiss them
try:
    not_now_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
    not_now_btn.click()
except:
    pass

try:
    not_now_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
    not_now_btn.click()
except:
    pass

# wait for the login to complete and the user dashboard to load
dashboard = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "Szr5J")))
print("Login successful!")
