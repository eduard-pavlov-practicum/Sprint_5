import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, LoginDialogLocators


class TestLogin:

    def test_login_successful(self, registered_user_email, password, open_login_form):
        driver = open_login_form
        driver.find_element(
            *LoginDialogLocators.EMAIL_FIELD).send_keys(registered_user_email)
        driver.find_element(
            *LoginDialogLocators.PASSWORD_FIELD).send_keys(password)

        driver.find_element(*LoginDialogLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.invisibility_of_element_located((LoginDialogLocators.ENTER_BUTTON)))
        assert driver.find_element(
            *StartPageLocators.AVATAR).is_displayed
        assert driver.find_element(
            *StartPageLocators.NAME).text == 'User.'
