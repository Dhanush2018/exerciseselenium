from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import email, password
from Driver import driver

class TestSearch:

    def testSearchProduct(self,driver):
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

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//button[@class='btn btn-default'])[1]"))).click()

        products = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='material-icons card_travel']"))).click()
        assert driver.title == "Automation Exercise - All Products"

        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID,"search_product")))
        search_box.send_keys("Tshirts")
        search_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID,"submit_search"))).click()

        searched_products_heading = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Searched Products']")))

        assert searched_products_heading.text == "SEARCHED PRODUCTS"

        products_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='features_items']")))

        products_list = products_container.find_elements(By.XPATH, "//div[contains(@class, 'product')]")

        # Assertion to ensure there is at least one product visible
        assert len(products_list) > 0, "No products found related to 'Tshirts'"
