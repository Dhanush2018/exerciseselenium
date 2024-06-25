from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import email, password
from Driver import driver

class TestAddProducts:

    def testAddProducts(self,driver):
        products = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='material-icons card_travel']"))).click()

        driver.execute_script("window.scrollBy(0, 500);")

        add_to_cart1 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//a[@class='btn btn-default add-to-cart'])[1]"))).click()

        continue_shopping = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-success close-modal btn-block']"))).click()

        add_to_cart2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//a[@class='btn btn-default add-to-cart'])[3]"))).click()

        view_cart = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//u[text()='View Cart']"))).click()

        tbody = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//tbody")))

        cart_items_elements = tbody.find_elements(By.XPATH, "./tr")

        # Assert that there are 2 items in the cart
        assert len(cart_items_elements) == 2, "Expected 2 items in the cart"

        # Iterate over each cart item element
        for item in cart_items_elements:
            item_name = item.find_element(By.XPATH, ".//td[@class='cart_product']").text
            item_quantity = item.find_element(By.XPATH, ".//td[@class='cart_quantity']").get_attribute('value')
            item_price = item.find_element(By.XPATH, ".//td[@class='cart_price']").text
            item_total = item.find_element(By.XPATH, ".//td[@class='cart_total']").text

            print(f"Item: {item_name}, Quantity: {item_quantity}, Price: {item_price}, Total: {item_total}")
