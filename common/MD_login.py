from selenium.webdriver.common.by import By



def resolution_login(driver, email, order):

    ele_email = driver.find_element(By.ID, "email-input")
    ele_email.send_keys(f'{email}')
    ele_orderNumber = driver.find_element(By.ID, "login-order-id-input")
    ele_orderNumber.send_keys(f'{order}')
    ele_button = driver.find_element(By.ID, "login_next")
    ele_button.click()
    element = driver.find_element(By.ID, "ready_to_submit").text

    return element



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
time.sleep(50)
driver.quit()