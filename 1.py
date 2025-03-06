import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import openpyxl
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("test_log.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("selenium_test")
logger.info('start')

# 读取测试数据
def read_txt(file_path):
    all_results = []
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            all_results.append(list(row))
    finally:
        workbook.close()
    return all_results

# 单个测试用例的执行函数
def test_login(data, url, chromedriver_path):
    try:
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)

        driver.get(url + data[0])
        assert "Resolution Center" in driver.title, "页面标题不正确"

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-email-input"))
        )
        email_input.send_keys(data[1])

        order_input = driver.find_element(By.ID, "login-order-id-input")
        order_input.send_keys(data[2])

        login_button = driver.find_element(By.ID, "login_next")
        login_button.click()

        ready_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ready_to_submit"))
        )
        assert "I'm ready to submit" in ready_button.text, "按钮文本不正确"

        logger.info(f"{data[0]} PASS")
    except Exception as e:
        logger.error(f"{data[0]} FAIL —— data: {data}", exc_info=True)
    finally:
        driver.quit()

# 多线程测试类
class MultiThreadedTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://example.com"  # 替换为你的测试 URL
        self.chromedriver_path = "/path/to/chromedriver"  # 替换为你的 chromedriver 路径
        self.data_file_path = "/Users/alex/登陆数据.xlsx"  # 替换为你的数据文件路径
        self.all_results = read_txt(self.data_file_path)

    def test_login_multi_threaded(self):
        # 使用线程池执行测试
        with ThreadPoolExecutor(max_workers=5) as executor:  # 可根据需要调整线程数
            futures = {executor.submit(test_login, data, self.url, self.chromedriver_path): data for data in self.all_results}
            for future in as_completed(futures):
                try:
                    future.result()  # 获取线程执行结果
                except Exception as e:
                    logger.error(f"线程执行失败: {e}", exc_info=True)

if __name__ == "__main__":
    unittest.main()