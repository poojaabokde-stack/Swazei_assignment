

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_002():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)

    driver.get("https://www.moneycontrol.com/")
    time.sleep(2)

    action = ActionChains(driver)

    # Hover on Login
    login = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//a[@title='Hello, Login']")))
    action.move_to_element(login).perform()

    # Click Log In
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@title='Log In']"))).click()


    wait.until(EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, "//iframe[contains(@src,'login')]")))

    # # Click "Login with Password"
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//button[contains(text(),'Login with Password')]"))).click()
    #
    # print("Clicked Login with Password successfully")
    #
    # driver.find_element(By.XPATH,"//input[@id='useremailel']").send_keys("poojaabokde@gmail.com")
    #
    # driver.find_element(By.XPATH, "//input[@id='userpassword']").send_keys("Pooja@1212")
    #
    # driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    #
    # print("Login successfully")
    #
    # driver.close()