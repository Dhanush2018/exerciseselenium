import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Driver import driver

class TestRemovingProductsFromCart:
    def testRPF(self,driver):
        add_to_cart = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//a[@class='btn btn-default add-to-cart'])[3]"))).click()
        view_cart = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//u[text()='View Cart']"))).click()
        cross_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='cart_quantity_delete']"))).click()
        time.sleep(4)