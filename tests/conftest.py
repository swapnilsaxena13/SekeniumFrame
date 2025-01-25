import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_service =Service("C:\\Users\\swapn\\.cache\\selenium\\chromedriver\\win64\\131.0.6778.85\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
    elif browser_name == "firefox":
        driver = webdriver.Firefox("C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
