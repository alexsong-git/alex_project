import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.chrome.service import Service
from data import chromedriver_path,url
import openpyxl
import time
from tool import read_txt

data = read_txt()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_log.log"),  # 将日志写入文件
        logging.StreamHandler()  # 同时输出日志到控制台
    ]
)
logger = logging.getLogger("selenium_test")
logger.info('start')

class Auto_Test(unittest.TestCase):


    def setUp(self):

        # 创建 Service 对象
        self.service=Service(executable_path=chromedriver_path)
        # 初始化 WebDriver
        self.driver=webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(3)  # 设置隐式等待时间为10秒

    def testlogin_1(self):

        for i in data:
            print(i)
            try:
                self.driver.get(url+i[0])
                self.assertIn("Resolution Center", self.driver.title)
                self.ele_email = self.driver.find_element(By.ID, "login-email-input")
                self.ele_email.send_keys(f'{i[1]}')
                self.ele_orderNumber = self.driver.find_element(By.ID, "login-order-id-input")
                self.ele_orderNumber.send_keys(f'{i[2]}')
                self.ele_button = self.driver.find_element(By.ID, "login_next")
                self.ele_button.click()
                #time.sleep(30)
                self.element = self.driver.find_element(By.ID, "ready_to_submit").text
                self.assertIn(self.element,"I'm ready to submit")
                logger.info(i[0] + " " + "PASS")
            except Exception as e:
                logger.info(i[0] + " " + "FAIL —— "+"data : "+f"{i}")
                #logger.info(e)
                continue


    def tearDown(self):

        self.driver.quit()
