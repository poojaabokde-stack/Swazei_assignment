import time
import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_moneycontrol_watchlist():
    driver = webdriver.Chrome()
    driver.maximize_window()


    # 1. Open Watchlist page
    driver.get("https://www.moneycontrol.com/watchlist/stocks")
    time.sleep(5)

    driver.find_element(By.XPATH,"//ul[contains(@class,'clearfix main_nav')]//a[@title='Watchlist'][normalize-space()='Watchlist']").click()
    time.sleep(1)

    driver.save_screenshot("D:\\pythonProject1\\Swazei_assignment\\screenshots\\test_003")
    time.sleep(2)

def count_existing_stocks(driver):
    stocks = driver.find_elements(By.XPATH, "//table//tbody//tr")
    count = len(stocks)
    print("Initial Watchlist Count:", count)
    return count

def read_stocks_from_csv():
    stock_list = []
    with open("D:\pythonProject1\Swazei_assignment\data\stocks.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            stock_list.append(row["stock"])
    return stock_list

def add_stocks_to_watchlist(driver, stocks):
    for stock in stocks:
        search_box = driver.find_element(By.XPATH, "//input[@id='search_str']")
        search_box.clear()
        search_box.send_keys(stock)
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='srch_tbl']//a").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//a[contains(text(),'Add to Watchlist')]").click()
        time.sleep(2)

        print(f"{stock} added to watchlist")

def count_final_stocks(driver):
    stocks = driver.find_elements(By.XPATH, "//table//tbody//tr")
    final_count = len(stocks)
    print("Final Watchlist Count:", final_count)
    return final_count