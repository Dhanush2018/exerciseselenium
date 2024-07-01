from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import email, user
from Driver import driver

class TestReview:
    def testReview(self,driver):

        driver.execute_script("window.scrollBy(0,500);")

        view_product = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//a[text() = 'View Product'])[2]"))).click()

        user_name = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"name")))
        user_name.send_keys(user)
        user_name.send_keys(Keys.RETURN)

        user_email = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"email")))
        user_email.send_keys(email)
        user_email.send_keys(Keys.RETURN)

        review = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"review")))
        review.send_keys("It is a very good product")
        review.send_keys(Keys.RETURN)

        submit = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"button-review"))).click()

        thanks_msg = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[text() = 'Thank you for your review.']")))

