import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, RegistrationDialogLocators


class TestRegistration:

    def test_registration_successful_avatar_and_name_visible(self, open_register_form, random_email, password):
        driver = open_register_form
        driver.find_element(RegistrationDialogLocators.EMAIL_FIELD['by'],
                            RegistrationDialogLocators.EMAIL_FIELD['locator']).send_keys(random_email)
        driver.find_element(RegistrationDialogLocators.PASSWORD_FIELD['by'],
                            RegistrationDialogLocators.PASSWORD_FIELD['locator']).send_keys(password)
        driver.find_element(RegistrationDialogLocators.PASSWORD_CONFIRMATION_FIELD['by'],
                            RegistrationDialogLocators.PASSWORD_CONFIRMATION_FIELD['locator']).send_keys(password)
        driver.find_element(RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['by'],
                            RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['locator']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.invisibility_of_element_located((RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['by'],
                                                                 RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['locator'])))
        assert driver.find_element(
            StartPageLocators.AVATAR['by'], StartPageLocators.AVATAR['locator']).is_displayed
        assert driver.find_element(
            StartPageLocators.NAME['by'], StartPageLocators.NAME['locator']).text == 'User.'

    @pytest.mark.parametrize(
        "email_type, process_email",
        [
            ("invalid email", "invalid_email"),
            ("existing email", "registered_user_email"),
        ],
        indirect=["process_email"]
    )
    def test_registration_unsuccessful_error_message_visible(self, email_type, process_email, password, open_register_form_for_existing_user):
        driver = open_register_form_for_existing_user
        driver.find_element(RegistrationDialogLocators.EMAIL_FIELD['by'],
                            RegistrationDialogLocators.EMAIL_FIELD['locator']).send_keys(process_email)
        driver.find_element(RegistrationDialogLocators.PASSWORD_FIELD['by'],
                            RegistrationDialogLocators.PASSWORD_FIELD['locator']).send_keys(password)
        driver.find_element(RegistrationDialogLocators.PASSWORD_CONFIRMATION_FIELD['by'],
                            RegistrationDialogLocators.PASSWORD_CONFIRMATION_FIELD['locator']).send_keys(password)
        driver.find_element(RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['by'],
                            RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['locator']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((RegistrationDialogLocators.ERROR_TEXT['by'],
                                                               RegistrationDialogLocators.ERROR_TEXT['locator'])))

        assert driver.find_element(RegistrationDialogLocators.ERROR_TEXT['by'],
                                   RegistrationDialogLocators.ERROR_TEXT['locator']).text == "Ошибка"
