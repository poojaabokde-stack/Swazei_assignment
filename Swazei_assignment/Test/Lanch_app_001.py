import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Launch_001():

    def test_001(self):
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.moneycontrol.com/")
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\Swazei_assignment\\screenshots\\test_launch_001")
        time.sleep(1)

        driver.close()



