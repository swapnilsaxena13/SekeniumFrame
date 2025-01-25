
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData[0])
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData[2])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[("Ayush","Saxena","Male"),("Swapnil","Saxena","Male")])
    def getData(self, request):
        return request.param

