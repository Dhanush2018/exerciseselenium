from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from Config import email, password
from Driver import driver

class TestBrandProducts:

    def testBrandProducts(self,driver):

        product = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//i[@class = 'material-icons card_travel']"))).click()

        driver.execute_script("window.scrollBy(0,500);")

        brand_1 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[text() = 'Babyhug']"))).click()

        babyhug = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h2[text() = 'Brand - Babyhug Products']")))

        assert babyhug.text == "BRAND - BABYHUG PRODUCTS"

        brand_2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text() = 'Allen Solly Junior']"))).click()

        allen = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h2[text() = 'Brand - Allen Solly Junior Products']")))

        assert allen.text == "BRAND - ALLEN SOLLY JUNIOR PRODUCTS"

