from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import email
from Driver import driver

class TestSubscription:

    def testSubscripation(self,driver):

        subscription = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h2[text()='Subscription']")))
        driver.execute_script("arguments[0].scrollIntoView();",subscription)

        assert subscription.text == "SUBSCRIPTION"

        email_address = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"susbscribe_email")))
        email_address.send_keys(email)
        email_address.send_keys(Keys.RETURN)

        successfully_subscripted = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"success-subscribe")))

        assert successfully_subscripted.text == "You have been successfully subscribed!"
        print(successfully_subscripted.text)