import pytest
from selenium import webdriver
from Config import url

@pytest.fixture(scope="module", params=["chrome"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
    else:
        raise ValueError("Unsupported browse!")
    yield driver
    driver.quit()