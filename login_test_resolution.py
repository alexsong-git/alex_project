import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from data import chromedriver_path,url_resolve,url_resolution,url_resolution_portal
from tool import read_txt
from log_tool import log_tool

path='/Users/alex/PycharmProjects/alex_project/test_log_resolution.log'
name='test_log_resolution'
log=log_tool(path,name)
data = read_txt()
data_twice=[]
class Auto_Test(unittest.TestCase):


    def setUp(self):

        # 创建 Service 对象
        self.service=Service(executable_path=chromedriver_path)
        # 初始化 WebDriver
        self.driver=webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(3)  # 设置隐式等待时间为10秒

    def testlogin(self):

        for i in data:
            print(i)
            try:
                self.driver.get(url_resolution)
                self.assertIn("Resolution Center", self.driver.title)
                self.ele_email = self.driver.find_element(By.ID, "login-email-input")
                self.ele_email.send_keys(f'{i[1]}')
                self.ele_orderNumber = self.driver.find_element(By.ID, "login-order-id-input")
                self.ele_orderNumber.send_keys(f'{i[2]}')
                self.ele_button = self.driver.find_element(By.ID, "login_next")
                self.ele_button.click()
                self.element = self.driver.find_element(By.ID, "ready_to_submit").text
                self.assertIn(self.element,"I'm ready to submit")
                #log.info(i[0] + " " + "PASS")
            except Exception as e:
                log.info(name+" "+i[0] + " " + "FAIL —— "+"data : "+f"{i}")
                #logger.info(e)
                data_twice.append(i)
                continue


    def tearDown(self):
        if data_twice !=[]:
            for i in data_twice:
                print(i)
                try:
                    self.driver.get(url_resolution)
                    self.assertIn("Resolution Center", self.driver.title)
                    self.ele_email = self.driver.find_element(By.ID, "login-email-input")
                    self.ele_email.send_keys(f'{i[1]}')
                    self.ele_orderNumber = self.driver.find_element(By.ID, "login-order-id-input")
                    self.ele_orderNumber.send_keys(f'{i[2]}')
                    self.ele_button = self.driver.find_element(By.ID, "login_next")
                    self.ele_button.click()
                    self.element = self.driver.find_element(By.ID, "ready_to_submit").text
                    self.assertIn(self.element, "I'm ready to submit")
                    log.info("twice : "+name+" "+i[0] + " " + "PASS")
                except Exception as e:
                    log.error("twice : "+name+" "+i[0] + " " + "FAIL —— " + "data : " + f"{i}")
                    # logger.info(e)
                    continue

        self.driver.quit()
