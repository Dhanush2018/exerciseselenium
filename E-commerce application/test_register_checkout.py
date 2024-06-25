from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import user, email, password, lastName,company, user_address, user_state,user_city,user_zipCode,user_mobile_num
import time
from Driver import driver

class TestRegCheckout:

    def test_reg_checkout(self,driver):

        add_to_cart = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH,"(//a[@class='btn btn-default add-to-cart'])[3]"))).click()

        continue_shopping = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success close-modal btn-block']"))).click()

        cart_icon = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH,"(//i[@class='fa fa-shopping-cart'])[1]"))).click()

        assert driver.title == "Automation Exercise - Checkout"

        checkout = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='btn btn-default check_out']"))).click()

        reg_login = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//u[text()='Register / Login']"))).click()

        user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "name")))
        user_name.send_keys(user)
        user_name.send_keys(Keys.RETURN)

        user_email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@name='email'])[2]")))
        user_email.send_keys(email)
        user_email.send_keys(Keys.RETURN)

        sign_up_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//button[@class='btn btn-default'])[2]"))).click()

        gender = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "uniform-id_gender1"))).click()

        creating_password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='form-control'])[3]")))
        creating_password.send_keys(password)
        creating_password.send_keys(Keys.RETURN)

        birth_date = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//select[@class='form-control'])[1]"))))
        birth_date.select_by_index(18)

        birth_month = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//select[@class='form-control'])[2]"))))
        birth_month.select_by_index(4)

        birth_year = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//select[@class='form-control'])[3]"))))
        birth_year.select_by_index(22)

        newsletter = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "// input[ @ name = 'newsletter']"))).click()
        special_offers = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='optin']"))).click()

        first_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "first_name")))
        first_name.send_keys(user)
        first_name.send_keys(Keys.RETURN)

        last_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "last_name")))
        last_name.send_keys(lastName)
        last_name.send_keys(Keys.RETURN)

        company_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "company")))
        company_name.send_keys(company)
        company_name.send_keys(Keys.RETURN)

        address = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='form-control'])[7]")))
        address.send_keys(user_address)
        address.send_keys(Keys.RETURN)

        country = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "country"))))
        country.select_by_index(1)

        state = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "state")))
        state.send_keys(user_state)
        state.send_keys(Keys.RETURN)

        city = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "city")))
        city.send_keys(user_city)
        city.send_keys(Keys.RETURN)

        zipcode = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "zipcode")))
        zipcode.send_keys(user_zipCode)
        zipcode.send_keys(Keys.RETURN)

        mobile_number = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mobile_number")))
        mobile_number.send_keys(user_mobile_num)
        mobile_number.send_keys(Keys.RETURN)

        create_acc = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-default'])[1]"))).click()

        assert driver.title == "Automation Exercise - Account Created"

        continue_ = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary']"))).click()

        user_logged_in = driver.find_element(By.XPATH, "//b[text()='Phoenix']")
        assert user_logged_in.is_displayed()

        cart_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-shopping-cart'])[1]"))).click()

        checkout = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@class='btn btn-default check_out']"))).click()

        comments = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//textarea[@class='form-control']")))
        comments.send_keys("Good Products")

        place_order = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Place Order']"))).click()

        name_on_card = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@class='form-control']")))
        name_on_card.send_keys(user)

        card_num = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@class='form-control card-number']")))
        card_num.send_keys("12345678900")

        cvc = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@class='form-control card-cvc']")))
        cvc.send_keys("181")

        expiry_month = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@class='form-control card-expiry-month']")))
        expiry_month.send_keys("05")

        expiry_yr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@class='form-control card-expiry-year']")))
        expiry_yr.send_keys("2030")

        conform_order = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"submit"))).click()

        #order_placed = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//div[@class='alert-success alert'])[1]")))
        #assert order_placed.text == "Your order has been placed successfully!"

        continuee = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='btn btn-primary']"))).click()

        delete_acc = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//i[@class='fa fa-trash-o']"))).click()

        continue_del = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='btn btn-primary']"))).click()


