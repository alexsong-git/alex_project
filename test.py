import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from data.rc_data  import chromedriver_path, url_resolution
from common.data_tool  import read_data
from common.log_tool import log_tool
import time

service=Service(executable_path=chromedriver_path)
driver=webdriver.Chrome(service=service)
driver.get('https://dashboard-dev.seel.com/login')
driver.implicitly_wait(5)
if 'Merchant Dashboard' == driver.title:
    print('yes')
else:
    print('no')
email=driver.find_element(By.ID,'email-input')
email.send_keys('yuchen.song+1200@seel.com')
button_1=driver.find_element(By.ID,'submit')
button_1.click()
password = driver.find_element(By.ID,'current-password')
password.send_keys('12345678ABbc!!')
button_2=driver.find_element(By.ID,'submit')
button_2.click()
print(driver.title)
time.sleep(5)
driver.quit()