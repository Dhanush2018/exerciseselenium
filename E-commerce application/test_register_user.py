from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import user, email, password, lastName,company, user_address, user_state,user_city,user_zipCode,user_mobile_num
import time
from Driver import driver

class TestRegister:

    def testRegisterUser(self, driver):
        sign_up = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//i[@class = 'fa fa-lock']"))).click()

        user_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"name")))
        user_name.send_keys(user)
        user_name.send_keys(Keys.RETURN)

        user_email = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//input[@name='email'])[2]")))
        user_email.send_keys(email)
        user_email.send_keys(Keys.RETURN)

        sign_up_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//button[@class='btn btn-default'])[2]"))).click()

        gender = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"uniform-id_gender1"))).click()

        creating_password = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//input[@class='form-control'])[3]")))
        creating_password.send_keys(password)
        creating_password.send_keys(Keys.RETURN)

        birth_date = Select(WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//select[@class='form-control'])[1]"))))
        birth_date.select_by_index(18)

        birth_month = Select(WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//select[@class='form-control'])[2]"))))
        birth_month.select_by_index(4)

        birth_year = Select(WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//select[@class='form-control'])[3]"))))
        birth_year.select_by_index(22)

        newsletter = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"// input[ @ name = 'newsletter']"))).click()
        special_offers = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@name='optin']"))).click()

        first_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"first_name")))
        first_name.send_keys(user)
        first_name.send_keys(Keys.RETURN)

        last_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"last_name")))
        last_name.send_keys(lastName)
        last_name.send_keys(Keys.RETURN)

        company_name =  WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"company")))
        company_name.send_keys(company)
        company_name.send_keys(Keys.RETURN)

        address = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//input[@class='form-control'])[7]")))
        address.send_keys(user_address)
        address.send_keys(Keys.RETURN)

        country = Select(WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"country"))))
        country.select_by_index(1)

        state = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"state")))
        state.send_keys(user_state)
        state.send_keys(Keys.RETURN)

        city = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"city")))
        city.send_keys(user_city)
        city.send_keys(Keys.RETURN)

        zipcode = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"zipcode")))
        zipcode.send_keys(user_zipCode)
        zipcode.send_keys(Keys.RETURN)

        mobile_number = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"mobile_number")))
        mobile_number.send_keys(user_mobile_num)
        mobile_number.send_keys(Keys.RETURN)

        create_acc = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//button[@class='btn btn-default'])[1]"))).click()

        assert driver.title == "Automation Exercise - Account Created"

        continue_ = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='btn btn-primary']"))).click()

        # delete_acc = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//i[@class='fa fa-trash-o']"))).click()
        #
        # continue_ = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary']"))).click()

        time.sleep(4)



