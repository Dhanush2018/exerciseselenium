from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import email, password
import time
from Driver import driver

class TestLogin():

    def testLoginUser(self,driver):
        log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class = 'fa fa-lock']"))).click()

        user_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@name='email'])[1]")))
        user_email.send_keys(email)
        user_email.send_keys(Keys.RETURN)

        password_ = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        password_.send_keys(password)
        password_.send_keys(Keys.RETURN)

        login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//button[@class='btn btn-default'])[1]"))).click()

        user_logged_in = driver.find_element(By.XPATH,"//b[text()='Phoenix']")
        assert user_logged_in.is_displayed()

        log_out = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//i[@class='fa fa-lock']"))).click()

        # delete_acc = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-trash-o']"))).click()
        #
        # continue_ = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary']"))).click()
        time.sleep(4)