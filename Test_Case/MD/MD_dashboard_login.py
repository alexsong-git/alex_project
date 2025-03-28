import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from data.rc_data  import chromedriver_path, url_md_dashboard
from common.data_tool  import read_data
from common.log_tool import log_tool


class Auto_Test(unittest.TestCase):


    def setUp(self):

        self.data = read_data("/Users/alex/登陆数据.xlsx","MD登陆数据")
        self.data_twice = []
        self.path= '/Users/alex/PycharmProjects/Seel_Project/test_report/MD_login'
        self.name='MD_login'
        self.log = log_tool(self.path, self.name)
        self.log.info('start')
        self.service=Service(executable_path=chromedriver_path)
        self.driver=webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(10)  # 设置隐式等待时间为10秒

    def tearDown(self):
        self.driver.quit()
        self.log.info('finish')

    def test_login(self):

        for channel, email, order in self.data:
            try:
                self.driver.get(url_md_dashboard)
                self.assertIn("Merchant Dashboard", self.driver.title)
                self.email = self.driver.find_element(By.ID, 'email-input')
                self.email.send_keys('yuchen.song+1200@seel.com')
                self.button_1 = self.driver.find_element(By.ID, 'submit')
                self.button_1.click()
                self.password = self.driver.find_element(By.ID, 'current-password')
                self.password.send_keys('12345678ABbc!!')
                self.button_2 = self.driver.find_element(By.ID, 'submit')
                self.button_2.click()
                self.element=self.driver.find_element(By.XPATH, "//h1[@class='font-bold text-3xl mr-6']").text
                print(self.element)
                self.assertIn(self.element, "Protection")
                # log.info(i[0] + " " + "PASS")
            except Exception as e:
                self.log.info(self.name+" "+channel + " " + "FAIL —— "+"data : "+ email+" "+order)
                # logger.info(e)
                self.data_twice.append([channel, email, order])
                continue