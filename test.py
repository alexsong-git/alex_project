from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

email='yuchen.song+1200@seel.com'
orderNumber='#1010'
result = f'Order: {orderNumber}'
url = 'https://resolution-dev.seel.com/customer-portal/'
chromedriver_path = "/usr/local/bin/chromedriver"
channel='shopline'

# 创建 Service 对象
service = Service(executable_path=chromedriver_path)
# 初始化 WebDriver
driver = webdriver.Chrome(service=service)
driver.get(url+channel)
ele_email = driver.find_element(By.ID, "email")
ele_email.send_keys(f'{email}')
ele_orderNumber = driver.find_element(By.ID, "orderNumber")
ele_orderNumber.send_keys(f'{orderNumber}')
ele_button=driver.find_element(By.XPATH, "//button/span[text()='Next']")
ele_button.click()
text = driver.find_element(By.CSS_SELECTOR, "div.font-bold.text-black.text-3xl").text
assert text==result
driver.quit()
print(text)
