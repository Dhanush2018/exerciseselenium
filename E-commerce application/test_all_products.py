from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import email, password
from Driver import driver

class TestProducts:

    def testAllProducts(self, driver):
        log_in = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class = 'fa fa-lock']"))).click()

        user_email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@name='email'])[1]")))
        user_email.send_keys(email)
        user_email.send_keys(Keys.RETURN)

        password_ = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        password_.send_keys(password)
        password_.send_keys(Keys.RETURN)

        products = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//i[@class='material-icons card_travel']"))).click()
        assert driver.title == "Automation Exercise - All Products"

        view_product = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//i[@class='fa fa-plus-square'])[1]"))).click()
        product_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h2[text()='Blue Top']")))
        category = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Category: Women > Tops']")))
        price = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Rs. 500']")))
        availability = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='product-details']//p[2]")))
        condition = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body//section//p[3]")))
        view_brand = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body//section//p[4]")))


