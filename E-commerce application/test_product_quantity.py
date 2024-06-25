import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import email, password
from Driver import driver

class TestQuantity:

    def testProductQuantity(self,driver):

        view_product = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//i[@class='fa fa-plus-square'])[2]"))).click()

        quantity = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"quantity")))
        quantity.clear()
        quantity.send_keys("4")

        add_to_cart = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//button[@class='btn btn-default cart']"))).click()

        view_cart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']"))).click()

        num_of_quantity = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//td[@class='cart_quantity']")))
        assert num_of_quantity.text == "4"
        print(num_of_quantity.text)
