from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import email, password, subject, message, user
import time
from Driver import driver

class TestContactUs():

    def testContactUs(self,driver):
        log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class = 'fa fa-lock']"))).click()

        user_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@name='email'])[1]")))
        user_email.send_keys(email)
        user_email.send_keys(Keys.RETURN)

        password_ = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        password_.send_keys(password)
        password_.send_keys(Keys.RETURN)

        login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//button[@class='btn btn-default'])[1]"))).click()

        contact_us = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//i[@class='fa fa-envelope']"))).click()

        get_in_touch = driver.find_element(By.XPATH,"// h2[text() = 'Get In Touch']")
        assert get_in_touch.is_displayed()

        name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"name")))
        name.send_keys(user)

        email_ = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"email")))
        email_.send_keys(email)

        subject_ = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"subject")))
        subject_.send_keys(subject)

        message_ = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"message")))
        message_.send_keys(message)

        driver.execute_script("window.scrollBy(0, 300);")

        upload_file = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//input[@class='form-control'])[4]")))
        upload_file.send_keys("C://Users/dhanush.srinivasa/Downloads/KARTHIK Resume.pdf")
        upload_file.send_keys(Keys.RETURN)

        time.sleep(4)