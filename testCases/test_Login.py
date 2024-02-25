
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_credKart_Login():

    def test_pageTitle_001(self,setup):
        self.driver = setup
        if self.driver.title == "CredKart":
            self.driver.save_screenshot(".\\ScreenShots\\test_pageTitle_001_Passed.PNG")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_pageTitle_001_Failed.PNG")
            self.driver.close()
            assert False

    def test_credKart_Login_002(self,setup):
        self.driver = setup
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credenceppb3@test.com")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        try:
            self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print("Login testcase is Passed")
            self.driver.save_screenshot(".\\ScreenShots\\test_credKart_Login_002_Passed.PNG")
            self.driver.close()
            assert True
        except:
            print("Login testcase is Failed")
            self.driver.save_screenshot(".\\ScreenShots\\test_credKart_Login_002_Failed.PNG")
            self.driver.close()
            assert False


































































































































































































































































