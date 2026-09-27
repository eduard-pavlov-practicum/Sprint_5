import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, LoginDialogLocators


class TestLogin:

    def test_login_successful(self, registered_user_email, password, open_login_form):
        driver = open_login_form
        driver.find_element(LoginDialogLocators.EMAIL_FIELD['by'],
                            LoginDialogLocators.EMAIL_FIELD['locator']).send_keys(registered_user_email)
        driver.find_element(LoginDialogLocators.PASSWORD_FIELD['by'],
                            LoginDialogLocators.PASSWORD_FIELD['locator']).send_keys(password)

        driver.find_element(LoginDialogLocators.ENTER_BUTTON['by'],
                            LoginDialogLocators.ENTER_BUTTON['locator']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.invisibility_of_element_located((LoginDialogLocators.ENTER_BUTTON['by'],
                                                                 LoginDialogLocators.ENTER_BUTTON['locator'])))
        assert driver.find_element(
            StartPageLocators.AVATAR['by'], StartPageLocators.AVATAR['locator']).is_displayed
        assert driver.find_element(
            StartPageLocators.NAME['by'], StartPageLocators.NAME['locator']).text == 'User.'
