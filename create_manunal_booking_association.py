from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import json
from dotenv import load_dotenv

# f = open('test_data.json')
# data = json.load(f)

load_dotenv()  # take environment variables from .env.

# for i in data['bookingDetails']:
#     bookingId = i["bookingId"]
#     lastName = i["lastName"]
#     departureDate = i["departureDate"]
#     print("bookingId, " ", lastName, " ", departureDate")

# Closing file
# f.close()

# Open URL
driver = webdriver.Chrome(options=Options())
driver.get("https://www.edp.pt")

# FINDING ELEMENTS BY ID
search_button = driver.find_element(
    By.ID, "onetrust-accept-btn-handler")

search_button.click()

# FINDING ELEMENTS BY X-PATH
login_button = driver.find_element(
    By.XPATH, "//li[@class='mainNavigation__btnLogin']//button")

login_button.click()

# TIME SLEEP
time.sleep(5)

# ACCEPT COOKIES
accept_cookie_login = driver.find_element(
    By.ID, "onetrust-accept-btn-handler")
accept_cookie_login.click()

# FILLING FORM
input_login = driver.find_element(By.XPATH, "//input[@id='form-email']")
# type the search string
input_login.send_keys(os.getenv("USERNAME"))

input_password = driver.find_element(By.XPATH, "//input[@id='form-password']")
# type the search string
input_password.send_keys(os.getenv("PASSWORD"))

# send enter key to get the search results!
button_enter = driver.find_element(
    By.XPATH, "//button[normalize-space()='Entrar']")
button_enter.click()
