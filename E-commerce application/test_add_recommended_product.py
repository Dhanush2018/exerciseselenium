import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import email, password
from Driver import driver

class TestAddToCart():
    def testAddToCartByRecommended(self,driver):

        recommended_item = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h2[text() = 'recommended items']")))
        driver.execute_script("arguments[0].scrollIntoView();", recommended_item)

        assert recommended_item.text == "RECOMMENDED ITEMS"

        add_to_cart = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//a[@class = 'btn btn-default add-to-cart'])[70]"))).click()

        view_cart = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//u[text() = 'View Cart']"))).click()

        product = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[text() = 'Men > Tshirts']")))













