from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from TestData.data import Saucedemo_Data
from TestLocator.locator import SauceDemo_locator

class Saucedemo_login:
    driver = webdriver.Chrome()

    def start(self):
        self.driver.implicitly_wait(10)
        self.driver.get(Saucedemo_Data.url)
        self.driver.maximize_window()
        return True
    
    def saucedemo_login(self):
        self.driver.find_element(by=By.ID, value= SauceDemo_locator.username_locator).send_keys(Saucedemo_Data.username)
        self.driver.find_element(by=By.ID, value= SauceDemo_locator.password_locator).send_keys(Saucedemo_Data.password)
        self.driver.find_element(by=By.ID, value= SauceDemo_locator.login_locator).click()
        return True
    
    def shutdown(self):
        self.driver.quit()
        return True