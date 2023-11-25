from selenium_profiles.webdriver import Chrome
from selenium_profiles.profiles import profiles
from selenium_driverless.webdriver import ChromeOptions
from selenium_driverless import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


profile = profiles.Windows()  # or .Android

options = ChromeOptions()
# options.add_argument("--headless=new")
driver = Chrome(profile, options=options, driverless_options=True)
driver.get('https://www.bet365.com.au/')  # test fingerprint

time.sleep(5)

login = driver.search_elements("/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[4]/div[3]")
login[0].click()

username = driver.search_elements("/html/body/div[1]/div/div[3]/div/div[2]/input")
username[0].write('*')

password = driver.search_elements("/html/body/div[1]/div/div[3]/div/div[3]/input")
password[0].write('*')

login_button = driver.search_elements("/html/body/div[1]/div/div[3]/div/div[4]")
time.sleep(0.5)
login_button[0].click()

time.sleep(5)
horse_racing = driver.search_elements("/html/body/div[1]/div/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div[5]/div[2]")
horse_racing[0].click()

time.sleep(5)
race1 = driver.search_elements("/html/body/div[1]/div/div[4]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[4]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div")
print(race1)
race1[0].click()