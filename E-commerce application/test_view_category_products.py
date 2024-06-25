import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Driver import driver

class TestVCP:
    def test_vcp(self,driver):

        driver.execute_script("window.scrollBy(0, 500);")
        category1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='badge pull-right'])[2]"))).click()
        tshirts = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Tshirts ']"))).click()
        result1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h2[text()='Men - Tshirts Products']")))
        assert result1.text == "MEN - TSHIRTS PRODUCTS"
        category2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='badge pull-right'])[3]"))).click()
        dress = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//a[text()='Dress '])[2]"))).click()
        result2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h2[@class='title text-center']")))
        assert result2.text == "KIDS - DRESS PRODUCTS"
        #abc
